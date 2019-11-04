'''

  -*- coding: utf-8 -*-

  library : PyQt5 UI code generator 5.11.2, matplotlib 2.2.2, librosa 0.7.1

  code by Soo-Hwan  :  https://github.com/sh951011/My-Capstone-Application
  blog : https://blog.naver.com/sooftware

  License : MIT License

'''

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog
import librosa
import torch
import numpy as np
import sounddevice as sd
from matplotlink import MatplotWidget

# AUDIO  ==
SAMPLE_RATE = 16000
N_FFT = 336
HOP_LENGTH = 84
# =======================

# MAIN WINDOW ==
MAIN_WINDOW_WIDTH = 750
MAIN_WINDOE_HEIGHT = 970
# =======================

# TEAMNAME ==
TEAMNAME_WIDTH = 250
TEAMNAME_HEIGHT = 31
TEAMNAME_COORD_X = 250
TEAMNAME_COORD_Y = 50
# =======================

# COMMENT ==
COMMENT_WIDTH = 500
COMMENT_HEIGHT = 55
COMMENT_COORD_X = 120
COMMENT_COORD_Y = 110
# =======================

# HEADER ==
HEADER_WIDTH = 300
HEADER_HEIGHT = 30
HEADER1_COORD_X = 100
HEADER1_COORD_Y = 200
HEADER2_COORD_X = HEADER1_COORD_X
HEADER2_COORD_Y = (HEADER1_COORD_Y + 105)
HEADER3_COORD_X = HEADER1_COORD_X
HEADER3_COORD_Y = (HEADER1_COORD_Y + 515)
# ========================

# LINE EDIT ==
EDIT_WIDTH = 350
EDIT_HEIGHT = 40
EDIT1_COORD_X = 100
EDIT1_COORD_Y = 240
EDIT2_COORD_X = EDIT1_COORD_X
EDIT2_COORD_Y = (EDIT1_COORD_Y + 410)
EDIT3_COORD_X = EDIT1_COORD_X
EDIT3_COORD_Y = (EDIT1_COORD_Y + 515)
EDIT1_DEFAULT = "Please upload audio file"
EDIT2_DEFAULT = "Please press Play button"
EDIT3_DEFAULT = "Infer retult by Kai Model"
# ========================

# BUTTON ==
BTN_WIDTH = 170
BTN_HEIGHT = EDIT_HEIGHT  # 40
LOAD_BTN_COORD_X = 470
LOAD_BTN_COORD_Y = EDIT1_COORD_Y
PLAY_BTN_COORD_X = LOAD_BTN_COORD_X
PLAY_BTN_COORD_Y = EDIT2_COORD_Y
INFER_BTN_COORD_X = LOAD_BTN_COORD_X
INFER_BTN_COORD_Y = EDIT3_COORD_Y
INIT_BTN_COORD_X = 285
INIT_BTN_COORD_Y = 835
# ========================

# PLOT & FOOTER ==
PLOT_WIDTH = 550
PLOT_HEIGHT = 300
PLOT_COORD_X = EDIT1_COORD_X
PLOT_COORD_Y = 340
FOOTER_COORD_X = 65
FOOTER_COORD_Y = 890
FOOTER_WIDTH = 600
FOOTER_HEIGHT = 70
# ======================

# FONT ==
MARGUN_FONT = "맑은 고딕"
NANUM_BOLD_FONT = "나눔스퀘어 ExtraBold"
HEADER_FONT_SIZE = 16
TEAMNAME_FONT_SIZE = 24
COMMENT_FONT_SIZE = 10
INIT_FONT_SIZE = 14
FOOTER_FONT_SIZE = 9
# ======================

class Prototype(object):
	def __init__(self):
		self.audio_path = None
		self.gt_path = None
		self.main_window = None

	def setup(self, main_window):
		# Basic Setting ==
		app = QtWidgets.QApplication(sys.argv)
		main_window.setObjectName("MainWindow")
		main_window.resize(MAIN_WINDOW_WIDTH, MAIN_WINDOE_HEIGHT)
		main_window.setWindowIcon(QIcon('icon2.png'))
		main_window.setMinimumSize(QtCore.QSize(MAIN_WINDOW_WIDTH, MAIN_WINDOE_HEIGHT))
		main_window.setMaximumSize(QtCore.QSize(MAIN_WINDOW_WIDTH, MAIN_WINDOE_HEIGHT))
		# Copied from https://github.com/jsgonzlez661/PyQt5-and-Matplotlib/main.py ==
		main_window.setStyleSheet("QLabel{\n"
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
		# ================================================
		self.centralwidget = QtWidgets.QWidget(main_window)
		self.centralwidget.setObjectName("centralwidget")
		# ============================

		# Team Name ===

		self.teamname_label = QtWidgets.QLabel(self.centralwidget)
		self.teamname_label.setGeometry(QtCore.QRect(TEAMNAME_COORD_X, TEAMNAME_COORD_Y, TEAMNAME_WIDTH, TEAMNAME_HEIGHT))
		font = QtGui.QFont(NANUM_BOLD_FONT)
		font.setPointSize(TEAMNAME_FONT_SIZE)
		self.teamname_label.setFont(font)
		self.teamname_label.setObjectName("teamname_label")
		self.teamname_label.setAlignment(QtCore.Qt.AlignCenter)

		# =============================

		# Comment ==

		self.comment = QtWidgets.QLabel(self.centralwidget)
		self.comment.setGeometry(QtCore.QRect(COMMENT_COORD_X, COMMENT_COORD_Y, COMMENT_WIDTH, COMMENT_HEIGHT))
		font = QtGui.QFont(MARGUN_FONT)
		font.setPointSize(COMMENT_FONT_SIZE)
		self.comment.setFont(font)
		self.comment.setObjectName("comment")
		self.comment.setAlignment(QtCore.Qt.AlignCenter)

		# =============================



		# 1. 음성파일 업로드 (Header1) ==

		self.header1 = QtWidgets.QLabel(self.centralwidget)
		self.header1.setGeometry(QtCore.QRect(HEADER1_COORD_X, HEADER1_COORD_Y, HEADER_WIDTH, HEADER_HEIGHT))
		font = QtGui.QFont(NANUM_BOLD_FONT)
		font.setPointSize(HEADER_FONT_SIZE)
		self.header1.setFont(font)
		self.header1.setObjectName("header1")
		self.edit1 = QtWidgets.QLineEdit(self.centralwidget)
		self.edit1.setGeometry(QtCore.QRect(EDIT1_COORD_X,  EDIT1_COORD_Y, EDIT_WIDTH, EDIT_HEIGHT))
		self.edit1.setObjectName("edit1")
		self.edit1.setText(EDIT1_DEFAULT)
		self.edit1.setStyleSheet("color: gray;")
		self.edit1.setAlignment(QtCore.Qt.AlignCenter)
		self.load_btn = QtWidgets.QPushButton(self.centralwidget)
		self.load_btn.setGeometry(QtCore.QRect(LOAD_BTN_COORD_X, LOAD_BTN_COORD_Y, BTN_WIDTH, BTN_HEIGHT))
		self.load_btn.setObjectName("load_btn1")

		# =============================

		# 2. 음성파일 확인 (Header2) ==

		self.header2 = QtWidgets.QLabel(self.centralwidget)
		self.header2.setGeometry(QtCore.QRect(HEADER2_COORD_X, HEADER2_COORD_Y, HEADER_WIDTH, HEADER_HEIGHT))
		font = QtGui.QFont(NANUM_BOLD_FONT)
		font.setPointSize(HEADER_FONT_SIZE)
		self.header2.setFont(font)
		self.header2.setObjectName("header2")
		self.matplot = MatplotWidget(self.centralwidget)
		self.matplot.setGeometry(QtCore.QRect(PLOT_COORD_X, PLOT_COORD_Y, PLOT_WIDTH, PLOT_HEIGHT))
		self.edit2 = QtWidgets.QLineEdit(self.centralwidget)
		self.edit2.setGeometry(QtCore.QRect(EDIT2_COORD_X, EDIT2_COORD_Y, EDIT_WIDTH, EDIT_HEIGHT))
		self.edit2.setObjectName("edit2")
		self.edit2.setText(EDIT2_DEFAULT)
		self.edit2.setStyleSheet("color: gray;")
		self.edit2.setAlignment(QtCore.Qt.AlignCenter)
		self.play_btn = QtWidgets.QPushButton(self.centralwidget)
		self.play_btn.setGeometry(QtCore.QRect(PLAY_BTN_COORD_X, PLAY_BTN_COORD_Y, BTN_WIDTH, BTN_HEIGHT))
		self.play_btn.setObjectName("play_btn")

		# =======================

		# 3. Kai 모델 인식 결과 (Header3) ==

		self.header3 = QtWidgets.QLabel(self.centralwidget)
		self.header3.setGeometry(QtCore.QRect(HEADER3_COORD_X, HEADER3_COORD_Y, HEADER_WIDTH, HEADER_HEIGHT))
		font = QtGui.QFont(NANUM_BOLD_FONT)
		font.setPointSize(HEADER_FONT_SIZE)
		self.header3.setFont(font)
		self.header3.setObjectName("header3")
		self.edit3 = QtWidgets.QLineEdit(self.centralwidget)
		self.edit3.setGeometry(QtCore.QRect(EDIT3_COORD_X, EDIT3_COORD_Y, EDIT_WIDTH, EDIT_HEIGHT))
		self.edit3.setObjectName("edit3")
		self.edit3.setText(EDIT3_DEFAULT)
		self.edit3.setStyleSheet("color: gray;")
		self.edit3.setAlignment(QtCore.Qt.AlignCenter)
		self.infer_btn = QtWidgets.QPushButton(self.centralwidget)
		self.infer_btn.setGeometry(QtCore.QRect(INFER_BTN_COORD_X, INFER_BTN_COORD_Y, BTN_WIDTH, BTN_HEIGHT))
		self.infer_btn.setObjectName("infer_btn")

		# =======================

		# 다시하기 버튼 ===

		self.init_btn = QtWidgets.QPushButton(self.centralwidget)
		self.init_btn.setGeometry(QtCore.QRect(INIT_BTN_COORD_X, INIT_BTN_COORD_Y, BTN_WIDTH, BTN_HEIGHT))
		self.init_btn.setObjectName("init_btn")
		font = QtGui.QFont(NANUM_BOLD_FONT)
		font.setPointSize(INIT_FONT_SIZE)
		self.init_btn.setFont(font)

		# =======================

		# 꼬리말 ===

		self.footer = QtWidgets.QLabel(self.centralwidget)
		self.footer.setGeometry(QtCore.QRect(FOOTER_COORD_X, FOOTER_COORD_Y, FOOTER_WIDTH, FOOTER_HEIGHT))
		font = QtGui.QFont(MARGUN_FONT)
		font.setPointSize(FOOTER_FONT_SIZE)
		self.footer.setFont(font)
		self.footer.setObjectName("footer")
		self.footer.setStyleSheet("color: gray;")
		self.footer.setAlignment(QtCore.Qt.AlignCenter)

		# =======================

		# Link Button to Func ==

		main_window.setCentralWidget(self.centralwidget)
		self.load_btn.clicked.connect(self.open_wav)
		self.play_btn.clicked.connect(self.play)
		self.init_btn.clicked.connect(self.initiate)

		# =======================

		def set_text(obj, main_window):
			translate = QtCore.QCoreApplication.translate
			main_window.setWindowTitle(translate("MainWindow", "Korean Speech Recognition"))
			obj.teamname_label.setText(translate("MainWindow", "Team Kai.Lib"))
			obj.comment.setText(translate("MainWindow", "음성파일을 업로드하여 인식결과를\n확인할 수 있는 시연용 프로토타입입니다."))
			obj.header1.setText(translate("MainWindow", "1. 음성파일 업로드"))
			obj.load_btn.setText(translate("MainWindow", "▦  Load"))
			obj.header2.setText(translate("MainWindow", "2. 음성파일 확인"))
			obj.play_btn.setText(translate("MainWindow", "▶  Play"))
			obj.header3.setText(translate("MainWindow", "3. Kai 모델 인식 결과"))
			obj.infer_btn.setText(translate("MainWindow", "\u2714  Infer"))
			obj.init_btn.setText(translate("MainWindow", "\u21bb"))
			obj.footer.setText(translate("MainWindow", "Team  Kai.Lib  Capstone  Project  of  2019\nAdvisor - Prof SuWon-Park"))
		set_text(self, main_window)
		QtCore.QMetaObject.connectSlotsByName(main_window)


	def open_wav(self):
		audio = QFileDialog.getOpenFileName(None, 'Audio File', "", "WAV File (*.wav)")
		self.edit1.setText(audio[0])
		self.audio_path = self.edit1.text()
		self.gt_path = self.audio_path.split('/')[-1].split('.')[0] + ".txt"

		def update_graph(obj):
			sig, sr = librosa.core.load(obj.audio_path, sr=SAMPLE_RATE)
			# remove silence ==
			non_silence_indices = librosa.effects.split(sig, top_db=30)
			sig = np.concatenate([sig[start:end] for start, end in non_silence_indices])
			# ======================

			# draw ==
			obj.matplot.canvas.axes.clear()
			obj.matplot.canvas.axes.plot(sig, color = 'skyblue')
			obj.matplot.canvas.axes.set_title("Audio Signal")
			obj.matplot.canvas.axes.set_xlabel("time")
			obj.matplot.canvas.axes.set_ylabel("Amplitude")
			obj.matplot.canvas.axes.grid(linewidth=0.2)
			obj.matplot.canvas.draw()
			# =======================
		update_graph(self)

	def play(self):
		def open_txt(obj):
			#text = QFileDialog.getOpenFileName(None, 'Text File', "", "TXT File (*.txt)")
			f = open(obj.gt_path, "r")
			contents = f.read()
			f.close()
			obj.edit2.setText(contents)

		def play_audio(obj):
			sig, sr = librosa.core.load(obj.audio_path, sr=SAMPLE_RATE)
			sd.play(sig, SAMPLE_RATE)

		open_txt(self)
		play_audio(self)

	def initiate(self):
		self.edit1.setText(EDIT1_DEFAULT)
		self.edit2.setText(EDIT2_DEFAULT)
		self.edit3.setText(EDIT3_DEFAULT)
		self.matplot.canvas.axes.clear()
		self.matplot.canvas.draw()
		self.audio_path = None
		self.gt_path = None

	def get_librosa_mfcc(filepath, n_mfcc=40, rm_silence=True):
		sig, sr = librosa.core.load(filepath, SAMPLE_RATE)
		# delete silence
		if rm_silence:
			non_silence_indices = librosa.effects.split(sig, top_db=30)
			sig = np.concatenate([sig[start:end] for start, end in non_silence_indices])
		mfccs = librosa.feature.mfcc(y=sig, sr=sr, hop_length=HOP_LENGTH, n_mfcc=n_mfcc, n_fft=N_FFT)

		return torch.FloatTensor(mfccs).transpose(0, 1)

import sys
app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
ui = Prototype()
ui.setup(main_window)
main_window.show()
sys.exit(app.exec_())