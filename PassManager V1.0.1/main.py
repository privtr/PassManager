from ui.login_ui import LoginUI 
from PySide2.QtWidgets import QApplication, QProxyStyle, QStyle

class Style(QProxyStyle):
    def drawPrimitive(self, element, option, painter, widget):
        if element == QStyle.PE_FrameFocusRect:
            return
        super().drawPrimitive(element, option, painter, widget)

if __name__ == '__main__':
	app = QApplication([])
	app.setStyle(Style())
	ui = LoginUI()
	app.exec_()
