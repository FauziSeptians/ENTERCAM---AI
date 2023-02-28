from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import Ui_MainWindow
from setFileName import setFileNameWindow
from setFilePath import SetFilePathWindow
import sys
import json

class mainProgram():
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.MainWindow = QtWidgets.QMainWindow()
		self.MainUi = Ui_MainWindow()
		self.MainUi.setupUi(self.MainWindow)
		self.assignMainUiFunc()
		self.MainWindow.show()
		sys.exit(self.appExec())

	def appExec(self):
		self.app.exec_()

		# stop thread capturer
		self.Capturer.stop()

	def assignMainUiFunc(self):
		# siapin animasi toggle
		self.MainUi.ObjectName1.clicked.connect(self.ObjectBtn1Toggle)
		self.MainUi.ObjectName2.clicked.connect(self.ObjectBtn2Toggle)
		self.MainUi.ObjectName3.clicked.connect(self.ObjectBtn3Toggle)
		self.MainUi.ObjectName4.clicked.connect(self.ObjectBtn4Toggle)

		# siapin json file
		self.json_file = open('last_settings.json')
		self.last_settings = json.load(self.json_file)

		# siapin kamera
		self.Capturer = Ui_MainWindow.FollowFrameCapturer()
		self.Capturer.start()
		self.Capturer.ImageUpdate.connect(self.ImageUpdateSlot)

		# siapin recorder
		self.Recorder = Ui_MainWindow.FollowFrameRecorder()
		self.Recorder.videoName = self.last_settings['video-name']
		self.Recorder.videoPath = self.last_settings['video-path']

		# siapin function button
		self.MainUi.StartRecordBtn.clicked.connect(self.StartRecord)
		self.MainUi.StopRecordBtn.clicked.connect(self.StopRecord)
		self.MainUi.SettingsBtn.clicked.connect(self.Settings)
		self.MainUi.ExitBtn.clicked.connect(self.Exit)

	def ObjectBtn1Toggle(self):
		if self.MainUi.ObjectName1.isChecked():
			self.MainUi.ObjectName1.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")
		else:
			self.MainUi.ObjectName1.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")

	def ObjectBtn2Toggle(self):
		if self.MainUi.ObjectName2.isChecked():
			self.MainUi.ObjectName2.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")
		else:
			self.MainUi.ObjectName2.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")

	def ObjectBtn3Toggle(self):
		if self.MainUi.ObjectName3.isChecked():
			self.MainUi.ObjectName3.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")
		else:
			self.MainUi.ObjectName3.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")

	def ObjectBtn4Toggle(self):
		if self.MainUi.ObjectName4.isChecked():
			self.MainUi.ObjectName4.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")
		else:
			self.MainUi.ObjectName4.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n")

	def ImageUpdateSlot(self, Image):
		self.MainUi.VideoFrame.setPixmap(QPixmap.fromImage(Image))

	def StartRecord(self):
		if self.MainUi.StartRecordBtn.isChecked():
			# buka window set file name
			self.startSetFileNameWindow()

			self.MainUi.StartRecordBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"}\n")
			self.MainUi.AirStatusText.setText("ON AIR")
			self.MainUi.AirStatus.setStyleSheet("background-color: rgba(0, 253, 71, 1);\nborder-radius: 5px")
		else:
			# tutup thread record
			self.Recorder.stop()

			self.MainUi.StartRecordBtn.setStyleSheet("QPushButton{\n"
"    background-color: #4E5058;\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"}\n"
)
			self.MainUi.AirStatusText.setText("OFF AIR")
			self.MainUi.AirStatus.setStyleSheet("background-color: red;\nborder-radius: 5px")

	def StopRecord(self):
		# tutup thread record
		self.Recorder.stop()

		self.MainUi.StartRecordBtn.setChecked(False)
		self.MainUi.StartRecordBtn.setStyleSheet("QPushButton{\n"
"    background-color: #4E5058;\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"}\n"
)
		self.MainUi.AirStatusText.setText("OFF AIR")
		self.MainUi.AirStatus.setStyleSheet("background-color: red;\nborder-radius: 5px")

	def Settings(self):
		self.startSetFilePathWindow()

	def Exit(self):
		self.Capturer.stop()
		sys.exit()

	def startSetFileNameWindow(self):
		self.setFileNameWindow = QtWidgets.QWidget()
		self.setFileNameUi = setFileNameWindow()
		self.setFileNameUi.setupUi(self.setFileNameWindow)
		self.setFileNameUi.FileName.setText(self.last_settings['video-name'])
		self.assignSetFileNameUiFunc()
		self.setFileNameWindow.show()

	def assignSetFileNameUiFunc(self):
		self.setFileNameUi.ConfirmBtn.clicked.connect(self.ConfirmSetFileName)
	
	def ConfirmSetFileName(self):
		self.Recorder.videoName = self.setFileNameUi.FileName.text()
		self.last_settings['video-name'] = self.setFileNameUi.FileName.text()
		print("Video name changed to: ", self.Recorder.videoName)
		self.Recorder.start()
		self.setFileNameWindow.close()

	def startSetFilePathWindow(self):
		self.setFilePathWindow = QtWidgets.QWidget()
		self.setFilePathUi = SetFilePathWindow()
		self.setFilePathUi.setupUi(self.setFilePathWindow)
		self.setFilePathUi.FilePath.setText(self.last_settings['video-path'])
		self.assignSetFilePathUiFunc()
		self.setFilePathWindow.show()

	def assignSetFilePathUiFunc(self):
		self.setFilePathUi.ConfirmBtn.clicked.connect(self.ConfirmSetFilePath)
	
	def ConfirmSetFilePath(self):
		self.Recorder.videoPath = self.setFilePathUi.FilePath.text()
		self.last_settings['video-path'] = self.setFilePathUi.FilePath.text()

		self.updateLastSettings()

		print("Video path changed to: ", self.Recorder.videoPath)
		self.setFilePathWindow.close()

	def updateLastSettings(self):
		with open('last_settings.json', 'w') as write_json_file:
			json.dump(self.last_settings, write_json_file)

if __name__ == "__main__":
	mainProgram = mainProgram()