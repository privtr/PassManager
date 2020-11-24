from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.main_ui import MainUI
from utils.login_logic import *

#Update
class LoginUI(QWidget):
	def __init__(self):
		super().__init__()

class LoginUI(QWidget):
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
		#Load widgets
		self.scrAdjustBtn()
		self.LoginWidgets()
		self.SignUpWidgets()
		self.hideSignUp()
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

	def LoginWidgets(self):
		#LineEdit Style
		style = ('QLineEdit{border: none; border-radius: 15px;\n'
			     		   'background-color: rgb(73, 80, 87);\n'
			     		   'color: rgb(255, 255, 255)}')
		#LineEdit Font
		font = QFont()
		font.setFamily('Segoe UI')
		font.setPointSize(12)
		#1 - edtUsernameL
		self.edtUsernameL = QLineEdit(self)
		self.edtUsernameL.setGeometry(250, 220, 200, 30)
		self.edtUsernameL.setAlignment(Qt.AlignCenter)
		self.edtUsernameL.setFont(font)
		self.edtUsernameL.setPlaceholderText('USERNAME')
		self.edtUsernameL.setStyleSheet(style)
		#2 - edtPasswordL
		self.edtPasswordL = QLineEdit(self)
		self.edtPasswordL.setGeometry(250, 260, 200, 30)
		self.edtPasswordL.setAlignment(Qt.AlignCenter)
		self.edtPasswordL.setFont(font)
		self.edtPasswordL.setPlaceholderText('PASSWORD')
		self.edtPasswordL.setStyleSheet(style)
		#PushButton Style
		style = ('QPushButton{border: none; border-radius: 5px;\n'
				             'background-color: rgb(52, 58, 64);\n'
				             'color: rgb(255, 255, 255)}\n'
				 'QPushButton:hover{background-color: rgb(60, 66, 72)}')
		#PushButton Font
		font.setBold(True)
		#3 - btnLogin
		self.btnLogin = QPushButton("LOGIN", self)
		self.btnLogin.clicked.connect(self.login)
		self.btnLogin.setFont(font)
		self.btnLogin.setGeometry(250, 320, 200, 30)
		self.btnLogin.setStyleSheet(style)
		#PushButton Style
		style = ('QPushButton{border: none; background: none; color: rgb(235, 235, 235);}\n'
				 'QPushButton:hover{color: rgb(255, 255, 255)}')
		#PushButton Font
		font.setBold(False)
		font.setUnderline(True)
		font.setPointSize(9)
		#4 - btnSignUpL
		self.btnSignUpL = QPushButton("SignUp?", self)
		self.btnSignUpL.clicked.connect(self.btnSignUpClick)
		self.btnSignUpL.setGeometry(328, 360, 44, 16)
		self.btnSignUpL.setFont(font)
		self.btnSignUpL.setStyleSheet(style)

	def SignUpWidgets(self):
		#LineEdit Style
		style = ('QLineEdit{border: none; border-radius: 15px;\n'
			     		   'background-color: rgb(73, 80, 87);\n'
			     		   'color: rgb(255, 255, 255)}')
		#LineEdit Font
		font = QFont()
		font.setFamily('Segoe UI')
		font.setPointSize(12)
		#1 - edtName
		self.edtName = QLineEdit(self)
		self.edtName.setGeometry(250, 150, 200, 30)
		self.edtName.setAlignment(Qt.AlignCenter)
		self.edtName.setFont(font)
		self.edtName.setPlaceholderText('NAME')
		self.edtName.setStyleSheet(style)
		#2 - edtSurname
		self.edtSurname = QLineEdit(self)
		self.edtSurname.setGeometry(250, 190, 200, 30)
		self.edtSurname.setAlignment(Qt.AlignCenter)
		self.edtSurname.setFont(font)
		self.edtSurname.setPlaceholderText('SURNAME')
		self.edtSurname.setStyleSheet(style)
		#3 - edtUsernameS
		self.edtUsernameS = QLineEdit(self)
		self.edtUsernameS.setGeometry(250, 230, 200, 30)
		self.edtUsernameS.setAlignment(Qt.AlignCenter)
		self.edtUsernameS.setFont(font)
		self.edtUsernameS.setPlaceholderText('USERNAME')
		self.edtUsernameS.setStyleSheet(style)
		#4 - edtPasswordS
		self.edtPasswordS = QLineEdit(self)
		self.edtPasswordS.setGeometry(250, 270, 200, 30)
		self.edtPasswordS.setAlignment(Qt.AlignCenter)
		self.edtPasswordS.setFont(font)
		self.edtPasswordS.setPlaceholderText('PASSWORD')
		self.edtPasswordS.setStyleSheet(style)
		#PushButton Style
		style = ('QPushButton{border: none; border-radius: 5px;\n'
				             'background-color: rgb(52, 58, 64);\n'
				             'color: rgb(255, 255, 255)}\n'
				 'QPushButton:hover{background-color: rgb(60, 66, 72)}')
		#PushButton Font
		font.setBold(True)
		#5 - btnSignUp
		self.btnSignUp = QPushButton("SignUp", self)
		self.btnSignUp.clicked.connect(self.signup)
		self.btnSignUp.setFont(font)
		self.btnSignUp.setGeometry(250, 330, 200, 30)
		self.btnSignUp.setStyleSheet(style)
		#PushButton Style
		style = ('QPushButton{border: none; background: none; color: rgb(235, 235, 235);}\n'
				 'QPushButton:hover{color: rgb(255, 255, 255)}')
		#PushButton font
		font.setBold(False)
		font.setUnderline(True)
		font.setPointSize(9)
		#6 - btnLoginS
		self.btnLoginS = QPushButton("Login?", self)
		self.btnLoginS.clicked.connect(self.btnLoginClick)
		self.btnLoginS.setGeometry(334, 370, 34, 16)
		self.btnLoginS.setFont(font)
		self.btnLoginS.setStyleSheet(style)

	def showLogin(self):
		self.edtUsernameL.show()
		self.edtPasswordL.show()
		self.btnLogin.show()
		self.btnSignUpL.show()

	def showSignUp(self):
		self.edtName.show()
		self.edtSurname.show()
		self.edtUsernameS.show()
		self.edtPasswordS.show()
		self.btnSignUp.show()
		self.btnLoginS.show()

	def hideLogin(self):
		self.edtUsernameL.hide()
		self.edtPasswordL.hide()
		self.btnLogin.hide()
		self.btnSignUpL.hide()

	def hideSignUp(self):
		self.edtName.hide()
		self.edtSurname.hide()
		self.edtUsernameS.hide()
		self.edtPasswordS.hide()
		self.btnSignUp.hide()
		self.btnLoginS.hide()

	def clearEdits(self):
		edtUsernameL.setText = ''
		edtPasswordL.setText = ''
		edtName.setText = ''
		edtSurname.setText = ''
		edtUsernameS.setText = ''
		edtPasswordL.setText = ''

	def btnLoginClick(self):
		self.clearEdits()
		self.showLogin()
		self.hideSignUp()

	def btnSignUpClick(self):
		self.clearEdits()
		self.hideLogin()
		self.showSignUp()

	def login(self):
		username = self.edtUsernameL.text()
		password = self.edtPasswordL.text()
		flag = isUserValid(username, password)
		if flag == True:
			self.close()
			self.next = MainUI()
		else: 
			self.edtUsernameL.setText('')
			self.edtPasswordL.setText('')

	def signup(self):
		username = self.edtUsernameS.text()
		flag = isUserAvailable(username)
		if flag == True:
			self.close()
			self.next = MainUI()
		else:
			self.edtUsernameS.setText('')

	def closeApp(self):
		self.close()

	def maximizeApp(self):
		pass

	def minimizeApp(self):
		self.showMinimized()
