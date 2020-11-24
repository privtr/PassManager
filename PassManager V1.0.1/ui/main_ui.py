from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
#from utils.main_logic import *

class MainUI(QWidget):
	def __init__(self):
		super().__init__()
		#Setup window specs
		self.setFixedSize(700, 500)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		#Setup background
		self.background = QFrame(self);
		self.background.setGeometry(0, 0, 700, 500)
		self.background.setStyleSheet("background-color: rgb(33, 37, 41);\n"
						   "border: none;")
		#Load Widgets
		self.scrAdjustBtn()
		self.loadSidePanel()
		self.GenPasswordWidgets()
		self.show()

	def scrAdjustBtn(self):
		self.btnClose = QPushButton(self)
		self.btnClose.clicked.connect(self.closeApp)
		self.btnClose.setGeometry(676, 6, 18, 18)
		self.btnClose.setStyleSheet('QPushButton{background: none; background-color: rgb(170, 0, 0);\n'
									'			 border: none; border-radius: 9px;}\n'
									'QPushButton:hover{background-color: rgb(230, 0, 0);}')
		self.btnMaximize = QPushButton(self)
		self.btnMaximize.clicked.connect(self.maximizeApp)
		self.btnMaximize.setGeometry(652, 6, 18, 18)
		self.btnMaximize.setStyleSheet('QPushButton{background: none; background-color: rgb(170, 0, 0);\n'
									   '			 border: none; border-radius: 9px;}\n'
									   'QPushButton:hover{background-color: rgb(230, 0, 0);}')
		self.btnMinimize = QPushButton(self)
		self.btnMinimize.clicked.connect(self.minimizeApp)
		self.btnMinimize.setGeometry(628, 6, 18, 18)
		self.btnMinimize.setStyleSheet('QPushButton{background: none; background-color: rgb(170, 0, 0);\n'
									   '			 border: none; border-radius: 9px;}\n'
									   'QPushButton:hover{background-color: rgb(230, 0, 0);}')

	def loadSidePanel(self):
		#Frame Style
		style = ('QFrame{background-color: rgb(25, 29, 33); border-top-left-radius: 10px;\n'
					   'border-bottom-left-radius: 10px; border: none;}')
		#1 - SidePanel
		self.SidePanel = QFrame(self)
		self.SidePanel.setGeometry(0, 0, 200, 500)
		self.SidePanel.setStyleSheet(style)
		#PushButton Style
		style = ('QPushButton{background: none; border: none; color: rgb(220, 220, 220)}\n'
				 'QPushButton:hover{background-color: rgb(35, 39, 43)}')
		#PushButton Font
		font = QFont()
		font.setFamily('Segoe UI')
		font.setPointSize(14)
		#2 - btnGenPassword
		self.btnGenPassword = QPushButton("Generate password", self)
		self.btnGenPassword.clicked.connect(self.showGenPassWidgets)
		self.btnGenPassword.setGeometry(0, 160, 200, 30)
		self.btnGenPassword.setStyleSheet(style)
		self.btnGenPassword.setFont(font)
		#3 - btnManagePassword
		self.btnManagePassword = QPushButton("Manage passwords", self)
		self.btnManagePassword.setGeometry(0, 200, 200, 30)
		self.btnManagePassword.setStyleSheet(style)
		self.btnManagePassword.setFont(font)

	def GenPasswordWidgets(self):
		#1 - lblTitle
		self.lblTitle = QLabel('Generate Password', self)
		self.lblTitle.hide()
		#2 - lblLenPassword
		self.lblLenPassword = QLabel('Length of password:', self)
		self.lblLenPassword.hide()
		#3 - edtLenPassword
		self.edtLenPassword = QLineEdit(self)
		self.edtLenPassword.hide()
		#4 - lblSpecChar
		self.lblSpecChar = QLabel('Do you want to use special characters:', self)
		self.lblSpecChar.hide()

	def showGenPassWidgets(self):
		self.lblTitle.show()
		self.lblLenPassword.show()
		self.edtLenPassword.show()
		self.lblSpecChar.show()

	def closeApp(self):
		self.close()

	def maximizeApp(self):
		pass

	def minimizeApp(self):
		self.showMinimized()
