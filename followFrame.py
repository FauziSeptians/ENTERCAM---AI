import cv2
from cvzone.PoseModule import PoseDetector
import numpy as np

detector = PoseDetector()

vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# biar bisa ubah frame size
frameSize = np.array([1280, 720])
vs.set(cv2.CAP_PROP_FRAME_WIDTH, frameSize[0])
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, frameSize[1])

ffSize = np.array([533, 300])
minSize = ffSize.copy()
maxSize = (max(frameSize), max(frameSize))

ffStart = np.array([0, 0])
offset = np.array([40, 40])

# videoWriter = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (ffSize[1], ffSize[0]))

def capture_follow_frame():
	global ffStart

	frame = vs.read()[1]

	img = frame.copy()
	img = detector.findPose(img, draw=False)
	bbox = detector.findPosition(img)[1]

	followFrame = frame.copy()

	if bbox:
		start = np.array([bbox['bbox'][0], bbox['bbox'][1]])
		end = np.array([bbox['bbox'][0] + bbox['bbox'][2], bbox['bbox'][1] + bbox['bbox'][3]])

		# biar koordinat object ga lewatin frame + offset
		if start[0] < offset[0]:
			start[0] = offset[0]
		if start[1] < offset[1]:
			start[1] = offset[1]
		if end[0] > frameSize[0] - offset[0]:
			end[0] = frameSize[0] - offset[0]
		if end[1] > frameSize[1] - offset[1]:
			end[1] = frameSize[1] - offset[1]

		# ubah size
		# fixSize = max(end[0] - start[0], end[1] - start[1])
		# size = np.array([fixSize, fixSize])

		# ffSize = size + 2 * offset

		# # biar ga lbh kecil dari size minimal
		# if np.all(size < minSize):
		# 	ffSize = minSize			

		# # biar ga lbh besar dri size maksimal
		# if np.all(size > maxSize):
		# 	ffSize = maxSize

		# print("Start: ", start)
		# print("End: ", end)

		# print(ffStart)

		ffEnd = ffStart + ffSize

		if np.any(start < (ffStart + offset)) or np.any(end > (ffEnd - offset)):
			# gerakin perlahan
			# klo start > ffStart, maka ffStart bertambah, gerak ke kanan
			# klo start < ffStart, maka ffStart berkurang, gerak ke kiri
			ffStart[0] += int((start[0] - ffStart[0] - offset[0]) / 8)
			ffStart[1] += int((start[1] - ffStart[1] - offset[1]) / 8)

			# gerakin langsung
			# ffStart = start - offset

			# set ulang ffEnd
			ffEnd = ffStart + ffSize

		# biar koordinat followFrame ga lewatin frame
		if ffStart[0] < 0:
			ffStart[0] = 0
			# set ulang ffEnd
			ffEnd = ffStart + ffSize
		if ffStart[1] < 0:
			ffStart[1] = 0
			ffEnd = ffStart + ffSize
		if ffStart[0] > frameSize[0] or ffEnd[0] > frameSize[0]:
			ffEnd[0] = frameSize[0]
			# set ulang ffStart
			ffStart = ffEnd - ffSize
		if ffStart[1] > frameSize[1] or ffEnd[1] > frameSize[1]:
			ffEnd[1] = frameSize[1]
			ffStart = ffEnd - ffSize

		# print("ffStart: ", ffStart)
		# print("ffEnd: ", ffEnd)

		followFrame = followFrame[ffStart[1]:ffEnd[1], ffStart[0]:ffEnd[0]]

	# videoWriter.write(followFrame)

	return followFrame