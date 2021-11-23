import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import tabs
import pyautogui
# from win32api import GetSystemMetrics
style = '''
QMenuBar{
    background-color: lightgray;
}

QTabBar::tab {
  padding: 8px;
}

QTabBar::tab:selected {
  background: white;
}
QPushButton{
    padding : 8px 20px;
}
QLineEdit#line1{
    height : 25px;
}
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        w, h = pyautogui.size()
        x = int(w/4)
        y = int(h/4)
        self.setGeometry(x,y, 700,600)
        self.setObjectName('MainWindow')
        pixmapi = getattr(QStyle, 'SP_DialogResetButton')
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.setWindowTitle("pupo")
        self.setStyleSheet(style)
        self.table_widget = tabs.MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.main_menu()

    def about_dev(self):
        title = 'Developers'
        text = 'Krekoten Roman\nNenarokomov Maxim'
        QMessageBox.about(self, title, text)

    def how_to_use(self):
        pass

    def main_menu(self):
        menubar = self.menuBar()
        menubar.addMenu('&File').addAction('Exit',exit)
        menubar.addMenu('&Option')

        about = menubar.addMenu('&About')
        about.addAction('Developers', self.about_dev)
        about.addAction('How to use?', self.how_to_use)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
