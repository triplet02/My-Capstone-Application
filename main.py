# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
import librosa
import torch
import numpy as np
import sounddevice as sd

SAMPLE_RATE = 16000
N_FFT = 336
HOP_LENGTH = 84

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		app = QtWidgets.QApplication(sys.argv)
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(541, 553)
		MainWindow.setWindowIcon(QIcon('icon2.png'))
		MainWindow.setMinimumSize(QtCore.QSize(541, 553))
		MainWindow.setMaximumSize(QtCore.QSize(541, 553))
		MainWindow.setStyleSheet("QLabel{\n"
		"/*color: white;*/\n"
		"}\n"
		"QPushButton{\n"
		"background-color: #54afcd;\n"
		"border-radius: 5px;\n"
		"color: white;\n"
		"}\n"
		"QPushButton:pressed{\n"
		"background-color: #359aca;\n"
		"border-radius: 5px;\n"
		"color: white;\n"
		"}\n"
		"QLineEdit{\n"
		"background-color: white;\n"
		"border-radius: 5px;\n"
		"}\n"
		"\n"
		"\n"
		"")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.teamname_label = QtWidgets.QLabel(self.centralwidget)
		self.teamname_label.setGeometry(QtCore.QRect(190, 0, 211, 31))
		font = QtGui.QFont("Arial")
		font.setPointSize(12)
		self.teamname_label.setFont(font)
		self.teamname_label.setObjectName("teamname_label")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(10, 60, 371, 31))
		self.lineEdit.setObjectName("lineEdit")
		self.load_btn1 = QtWidgets.QPushButton(self.centralwidget)
		self.load_btn1.setGeometry(QtCore.QRect(390, 60, 141, 31))
		self.load_btn1.setObjectName("load_btn1")
		self.play_btn = QtWidgets.QPushButton(self.centralwidget)
		self.play_btn.setGeometry(QtCore.QRect(205, 510, 141, 31))
		self.play_btn.setObjectName("load_btn1")
		self.audio_label = QtWidgets.QLabel(self.centralwidget)
		self.audio_label.setGeometry(QtCore.QRect(100, 40, 171, 16))
		self.infer_label = QtWidgets.QLabel(self.centralwidget)
		self.infer_label.setGeometry(QtCore.QRect(120, 160, 171, 16))
		font = QtGui.QFont('SansSerif')
		font.setPointSize(10)
		self.audio_label.setFont(font)
		self.audio_label.setObjectName("audio_label")
		self.infer_label.setFont(font)
		self.infer_label.setObjectName("infer_label")
		self.load_btn2 = QtWidgets.QPushButton(self.centralwidget)
		self.load_btn2.setGeometry(QtCore.QRect(390, 120, 141, 31))
		self.load_btn2.setObjectName("load_btn2")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 371, 31))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.gt_label = QtWidgets.QLabel(self.centralwidget)
		self.gt_label.setGeometry(QtCore.QRect(90, 100, 221, 16))
		font = QtGui.QFont('SansSerif')
		font.setPointSize(10)
		self.gt_label.setFont(font)
		self.gt_label.setObjectName("gt_label")
		self.MplWidget = MplWidget(self.centralwidget)
		self.MplWidget.setGeometry(QtCore.QRect(10, 210, 520, 300))
		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 371, 31))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.infer_btn = QtWidgets.QPushButton(self.centralwidget)
		self.infer_btn.setGeometry(QtCore.QRect(390, 180, 141, 31))
		self.infer_btn.setObjectName("infer_btn")
		MainWindow.setCentralWidget(self.centralwidget)
		self.load_btn1.clicked.connect(self.open_wav)
		self.load_btn2.clicked.connect(self.open_txt)
		self.play_btn.clicked.connect(self.play_audio)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Korean Speech Recognition"))
		self.teamname_label.setText(_translate("MainWindow", "    Team Kai.Lib"))
		self.load_btn1.setText(_translate("MainWindow", "Load"))
		self.audio_label.setText(_translate("MainWindow", "Upload audio file (wav)"))
		self.infer_label.setText(_translate("MainWindow", "Infer by Model"))
		self.load_btn2.setText(_translate("MainWindow", "Load"))
		self.play_btn.setText(_translate("MainWindow", " ▶ "))
		self.gt_label.setText(_translate("MainWindow", "    Ground Truth (txt)"))
		self.infer_btn.setText(_translate("MainWindow", "Infer"))
		#self.infer_btn.clicked.connect(self.update_graph)

	def open_wav(self):
		audio = QFileDialog.getOpenFileName(None, 'Audio File', "", "WAV File (*.wav)")
		self.lineEdit.setText(audio[0].split('/')[-1])

		def update_graph(obj):
			audio_path = obj.lineEdit.text()
			sig, sr = librosa.core.load(audio_path, sr=SAMPLE_RATE)
			self.MplWidget.canvas.axes.clear()
			self.MplWidget.canvas.axes.plot(sig, color = 'skyblue')
			self.MplWidget.canvas.axes.legend(["Signal"], loc='upper right')
			self.MplWidget.canvas.axes.set_title("Audio Signal")
			self.MplWidget.canvas.axes.set_ylabel("Amplitude")
			self.MplWidget.canvas.axes.grid(linewidth=0.2)
			self.MplWidget.canvas.draw()

		update_graph(self)

	def open_txt(self):
		text = QFileDialog.getOpenFileName(None, 'Text File', "", "TXT File (*.txt)")
		f = open(text[0], "r")
		contents = f.read()
		f.close()
		self.lineEdit_2.setText(contents)

	def play_audio(self):
		audio_path = self.lineEdit.text()
		sig, sr = librosa.core.load(audio_path, sr=SAMPLE_RATE)
		sd.play(sig, 16000)

	def get_librosa_mfcc(filepath, n_mfcc=40, rm_silence=True):
		sig, sr = librosa.core.load(filepath, SAMPLE_RATE)
		# delete silence
		if rm_silence:
			non_silence_indices = librosa.effects.split(sig, top_db=30)
			sig = np.concatenate([sig[start:end] for start, end in non_silence_indices])
		mfccs = librosa.feature.mfcc(y=sig, sr=sr, hop_length=HOP_LENGTH, n_mfcc=n_mfcc, n_fft=N_FFT)

		return torch.FloatTensor(mfccs).transpose(0, 1)

from mplwidget import MplWidget


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())