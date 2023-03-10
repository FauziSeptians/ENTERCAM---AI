# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
from followFrame import capture_follow_frame

# untuk capture dan record
frame = None

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1280, 720)
		MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
		MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(25, 27, 38))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(25, 27, 38))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(25, 27, 38))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
		MainWindow.setPalette(palette)
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(8)
		MainWindow.setFont(font)
		MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.VideoFrame = QtWidgets.QLabel(self.centralwidget)
		self.VideoFrame.setEnabled(True)
		self.VideoFrame.setGeometry(QtCore.QRect(266, 20, 748, 439))
		self.VideoFrame.setStyleSheet("background-color: rgba(217, 217, 217, 0.2);")
		self.VideoFrame.setText("")
		self.VideoFrame.setObjectName("VideoFrame")
		self.ObjectLabel = QtWidgets.QLabel(self.centralwidget)
		self.ObjectLabel.setGeometry(QtCore.QRect(11, 480, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.ObjectLabel.setFont(font)
		self.ObjectLabel.setStyleSheet("background-color: #D9D9D9;\n"
"border-radius: 3px;")
		self.ObjectLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.ObjectLabel.setObjectName("ObjectLabel")
		self.AudioLabel = QtWidgets.QLabel(self.centralwidget)
		self.AudioLabel.setGeometry(QtCore.QRect(434, 480, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.AudioLabel.setFont(font)
		self.AudioLabel.setStyleSheet("background-color: #D9D9D9;\n"
"border-radius: 3px;")
		self.AudioLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.AudioLabel.setObjectName("AudioLabel")
		self.ControlsLabel = QtWidgets.QLabel(self.centralwidget)
		self.ControlsLabel.setGeometry(QtCore.QRect(857, 480, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.ControlsLabel.setFont(font)
		self.ControlsLabel.setStyleSheet("background-color: #D9D9D9;\n"
"border-radius: 3px;")
		self.ControlsLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.ControlsLabel.setObjectName("ControlsLabel")
		self.ObjectBackground = QtWidgets.QLabel(self.centralwidget)
		self.ObjectBackground.setEnabled(True)
		self.ObjectBackground.setGeometry(QtCore.QRect(11, 480, 412, 300))
		self.ObjectBackground.setStyleSheet("background-color: #2B2E38;\n"
"border-radius: 3px;")
		self.ObjectBackground.setText("")
		self.ObjectBackground.setObjectName("ObjectBackground")
		self.AudioBackground = QtWidgets.QLabel(self.centralwidget)
		self.AudioBackground.setEnabled(True)
		self.AudioBackground.setGeometry(QtCore.QRect(434, 480, 412, 300))
		self.AudioBackground.setStyleSheet("background-color: #2B2E38;\n"
"border-radius: 3px;")
		self.AudioBackground.setText("")
		self.AudioBackground.setObjectName("AudioBackground")
		self.ControlsBackground = QtWidgets.QLabel(self.centralwidget)
		self.ControlsBackground.setEnabled(True)
		self.ControlsBackground.setGeometry(QtCore.QRect(857, 480, 412, 300))
		self.ControlsBackground.setStyleSheet("background-color: #2B2E38;\n"
"border-radius: 3px;")
		self.ControlsBackground.setText("")
		self.ControlsBackground.setObjectName("ControlsBackground")
		self.AirStatusText = QtWidgets.QLabel(self.centralwidget)
		self.AirStatusText.setGeometry(QtCore.QRect(1195, 680, 55, 16))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(6)
		self.AirStatusText.setFont(font)
		self.AirStatusText.setStyleSheet("color: rgba(217, 217, 217, 1);")
		self.AirStatusText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.AirStatusText.setObjectName("AirStatusText")
		self.AirStatus = QtWidgets.QLabel(self.centralwidget)
		self.AirStatus.setGeometry(QtCore.QRect(1255, 684, 10, 10))
		self.AirStatus.setStyleSheet("background-color: red;\n"
"border-radius: 5px;")
		self.AirStatus.setText("")
		self.AirStatus.setObjectName("AirStatus")
		self.ObjectName1 = QtWidgets.QPushButton(self.centralwidget)
		self.ObjectName1.setGeometry(QtCore.QRect(11, 520, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.ObjectName1.setFont(font)
		self.ObjectName1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.ObjectName1.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.ObjectName1.setCheckable(True)
		self.ObjectName1.setChecked(False)
		self.ObjectName1.setObjectName("ObjectName1")
		self.ObjectName2 = QtWidgets.QPushButton(self.centralwidget)
		self.ObjectName2.setGeometry(QtCore.QRect(11, 560, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.ObjectName2.setFont(font)
		self.ObjectName2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.ObjectName2.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.ObjectName2.setCheckable(True)
		self.ObjectName2.setChecked(False)
		self.ObjectName2.setObjectName("ObjectName2")
		self.ObjectName3 = QtWidgets.QPushButton(self.centralwidget)
		self.ObjectName3.setGeometry(QtCore.QRect(11, 600, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.ObjectName3.setFont(font)
		self.ObjectName3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.ObjectName3.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.ObjectName3.setCheckable(True)
		self.ObjectName3.setChecked(False)
		self.ObjectName3.setObjectName("ObjectName3")
		self.ObjectName4 = QtWidgets.QPushButton(self.centralwidget)
		self.ObjectName4.setGeometry(QtCore.QRect(11, 640, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.ObjectName4.setFont(font)
		self.ObjectName4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.ObjectName4.setStyleSheet("QPushButton{\n"
"    background-color: rgba(40, 76, 184, 0);\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"    padding: 0px 10px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.ObjectName4.setCheckable(True)
		self.ObjectName4.setChecked(False)
		self.ObjectName4.setObjectName("ObjectName4")
		self.StartRecordBtn = QtWidgets.QPushButton(self.centralwidget)
		self.StartRecordBtn.setGeometry(QtCore.QRect(857, 520, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.StartRecordBtn.setFont(font)
		self.StartRecordBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.StartRecordBtn.setStyleSheet("QPushButton{\n"
"    background-color: #4E5058;\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.StartRecordBtn.setCheckable(True)
		self.StartRecordBtn.setChecked(False)
		self.StartRecordBtn.setObjectName("StartRecordBtn")
		self.StopRecordBtn = QtWidgets.QPushButton(self.centralwidget)
		self.StopRecordBtn.setGeometry(QtCore.QRect(857, 560, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.StopRecordBtn.setFont(font)
		self.StopRecordBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.StopRecordBtn.setStyleSheet("QPushButton{\n"
"    background-color: #4E5058;\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.StopRecordBtn.setCheckable(True)
		self.StopRecordBtn.setChecked(False)
		self.StopRecordBtn.setObjectName("StopRecordBtn")
		self.SettingsBtn = QtWidgets.QPushButton(self.centralwidget)
		self.SettingsBtn.setGeometry(QtCore.QRect(857, 600, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.SettingsBtn.setFont(font)
		self.SettingsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.SettingsBtn.setStyleSheet("QPushButton{\n"
"    background-color: #4E5058;\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.SettingsBtn.setCheckable(False)
		self.SettingsBtn.setChecked(False)
		self.SettingsBtn.setObjectName("Settings")
		self.ExitBtn = QtWidgets.QPushButton(self.centralwidget)
		self.ExitBtn.setGeometry(QtCore.QRect(857, 640, 412, 38))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(10)
		self.ExitBtn.setFont(font)
		self.ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.ExitBtn.setStyleSheet("QPushButton{\n"
"    background-color: #4E5058;\n"
"    color: rgba(217, 217, 217, 1);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgba(40, 76, 184, 0.4);\n"
"}")
		self.ExitBtn.setCheckable(True)
		self.ExitBtn.setChecked(False)
		self.ExitBtn.setObjectName("Exit")
		self.Audio1 = QtWidgets.QLabel(self.centralwidget)
		self.Audio1.setGeometry(QtCore.QRect(444, 530, 101, 16))
		self.Audio1.setStyleSheet("color: rgba(217, 217, 217, 1);")
		self.Audio1.setObjectName("Audio1")
		self.AudioVolume1 = QtWidgets.QLabel(self.centralwidget)
		self.AudioVolume1.setGeometry(QtCore.QRect(444, 552, 390, 5))
		self.AudioVolume1.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
		self.AudioVolume1.setText("")
		self.AudioVolume1.setPixmap(QtGui.QPixmap("BAR.png"))
		self.AudioVolume1.setScaledContents(True)
		self.AudioVolume1.setObjectName("AudioVolume1")
		self.AudioSlider1 = QtWidgets.QSlider(self.centralwidget)
		self.AudioSlider1.setGeometry(QtCore.QRect(444, 570, 300, 10))
		self.AudioSlider1.setStyleSheet("QScrollBar::handle{\n"
"    background: rgba(217, 217, 217, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle::pressed{\n"
"    background: rgba(217, 217, 217, 0);\n"
"}")
		self.AudioSlider1.setOrientation(QtCore.Qt.Horizontal)
		self.AudioSlider1.setInvertedAppearance(False)
		self.AudioSlider1.setInvertedControls(False)
		self.AudioSlider1.setObjectName("AudioSlider1")
		self.Audio2 = QtWidgets.QLabel(self.centralwidget)
		self.Audio2.setGeometry(QtCore.QRect(444, 585, 101, 16))
		self.Audio2.setStyleSheet("color: rgba(217, 217, 217, 1);")
		self.Audio2.setObjectName("Audio2")
		self.AudioSlider2 = QtWidgets.QSlider(self.centralwidget)
		self.AudioSlider2.setGeometry(QtCore.QRect(444, 625, 300, 10))
		self.AudioSlider2.setStyleSheet("QScrollBar::handle{\n"
"    background: rgba(217, 217, 217, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle::pressed{\n"
"    background: rgba(217, 217, 217, 0);\n"
"}")
		self.AudioSlider2.setOrientation(QtCore.Qt.Horizontal)
		self.AudioSlider2.setInvertedAppearance(False)
		self.AudioSlider2.setInvertedControls(False)
		self.AudioSlider2.setObjectName("AudioSlider2")
		self.AudioVolume2 = QtWidgets.QLabel(self.centralwidget)
		self.AudioVolume2.setGeometry(QtCore.QRect(444, 607, 390, 5))
		self.AudioVolume2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
		self.AudioVolume2.setText("")
		self.AudioVolume2.setPixmap(QtGui.QPixmap("BAR.png"))
		self.AudioVolume2.setScaledContents(True)
		self.AudioVolume2.setObjectName("AudioVolume2")
		self.Audio3 = QtWidgets.QLabel(self.centralwidget)
		self.Audio3.setGeometry(QtCore.QRect(444, 640, 101, 16))
		self.Audio3.setStyleSheet("color: rgba(217, 217, 217, 1);")
		self.Audio3.setObjectName("Audio3")
		self.AudioSlider3 = QtWidgets.QSlider(self.centralwidget)
		self.AudioSlider3.setGeometry(QtCore.QRect(444, 680, 300, 10))
		self.AudioSlider3.setStyleSheet("QScrollBar::handle{\n"
"    background: rgba(217, 217, 217, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle::pressed{\n"
"    background: rgba(217, 217, 217, 0);\n"
"}")
		self.AudioSlider3.setOrientation(QtCore.Qt.Horizontal)
		self.AudioSlider3.setInvertedAppearance(False)
		self.AudioSlider3.setInvertedControls(False)
		self.AudioSlider3.setObjectName("AudioSlider3")
		self.AudioVolume3 = QtWidgets.QLabel(self.centralwidget)
		self.AudioVolume3.setGeometry(QtCore.QRect(444, 662, 390, 5))
		self.AudioVolume3.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
		self.AudioVolume3.setText("")
		self.AudioVolume3.setPixmap(QtGui.QPixmap("BAR.png"))
		self.AudioVolume3.setScaledContents(True)
		self.AudioVolume3.setObjectName("AudioVolume3")
		self.ObjectBackground.raise_()
		self.ControlsBackground.raise_()
		self.AudioBackground.raise_()
		self.VideoFrame.raise_()
		self.ObjectLabel.raise_()
		self.AudioLabel.raise_()
		self.ControlsLabel.raise_()
		self.AirStatusText.raise_()
		self.AirStatus.raise_()
		self.ObjectName1.raise_()
		self.ObjectName2.raise_()
		self.ObjectName3.raise_()
		self.ObjectName4.raise_()
		self.StartRecordBtn.raise_()
		self.StopRecordBtn.raise_()
		self.SettingsBtn.raise_()
		self.ExitBtn.raise_()
		self.Audio1.raise_()
		self.AudioVolume1.raise_()
		self.AudioSlider1.raise_()
		self.Audio2.raise_()
		self.AudioSlider2.raise_()
		self.AudioVolume2.raise_()
		self.Audio3.raise_()
		self.AudioSlider3.raise_()
		self.AudioVolume3.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Entertainment Moving Camera"))
		self.ObjectLabel.setText(_translate("MainWindow", "OBJECT"))
		self.AudioLabel.setText(_translate("MainWindow", "AUDIO"))
		self.ControlsLabel.setText(_translate("MainWindow", "CONTROLS"))
		self.AirStatusText.setText(_translate("MainWindow", "OFF AIR"))
		self.ObjectName1.setText(_translate("MainWindow", "Mikel Oktavioni"))
		self.ObjectName2.setText(_translate("MainWindow", "Christina Vanesius"))
		self.ObjectName3.setText(_translate("MainWindow", "Fauzi Tanutomo"))
		self.ObjectName4.setText(_translate("MainWindow", "Kezia Putri"))
		self.StartRecordBtn.setText(_translate("MainWindow", "Start Record"))
		self.StopRecordBtn.setText(_translate("MainWindow", "Stop Record"))
		self.SettingsBtn.setText(_translate("MainWindow", "Settings"))
		self.ExitBtn.setText(_translate("MainWindow", "Exit"))
		self.Audio1.setText(_translate("MainWindow", "Mic Singer - 1"))
		self.Audio2.setText(_translate("MainWindow", "Mic Singer - 2"))
		self.Audio3.setText(_translate("MainWindow", "Mic Singer - 3"))

	class FollowFrameCapturer(QThread):
		ImageUpdate = pyqtSignal(QImage)

		def run(self):
			global frame
			self.ThreadActive = True

			while self.ThreadActive:
				frame = capture_follow_frame()
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				frame = cv2.resize(frame, (748, 439))
				QtFrame = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
				QtFrame = QtFrame.scaled(748, 439, Qt.KeepAspectRatio)
				self.ImageUpdate.emit(QtFrame)

		def stop(self):
			self.ThreadActive = False
			self.quit()

	class FollowFrameRecorder(QThread):
		videoPath = "D:\PPTI 11\Kuliah\Cawu 3\Artificial Intelligence\Tugas\Project AI\App Jadi\Records\\"
		videoName = "video"

		def run(self):
			global frame

			self.ThreadActive = True
			self.videoWriter = cv2.VideoWriter(self.videoPath + self.videoName + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (533, 300))

			while self.ThreadActive:
				self.videoWriter.write(frame)

		def stop(self):
			self.ThreadActive = False
			self.videoWriter.release()
			self.quit()