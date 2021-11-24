import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import tabs
from platform import platform
# import pyautogui

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
QLineEdit{
    height: 23px;
}
QProgressBar{
    height: 25px;
}
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        x = int(1920/3)
        y = int(1080/3)
        self.setGeometry(x,y, 700,600)
        self.setObjectName('MainWindow')
        pixmapi = getattr(QStyle, 'SP_FileDialogNewFolder')
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.setWindowTitle("pupo")
        self.setStyleSheet(style)
        self.table_widget = tabs.MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.main_menu()


    def about_dev(self):
        title = 'About'
        text = f'''
        Programm to Use Program Operations (Pupo)
        Version: 2.1.0
        Update: 2021-11-24 12:38:02
        OS: {platform()} 64-bit
        @Scientific and Production Association RadioSignal JSC
        Software engineers: Krekoten Roman, Nenarokomov Maxim
        '''
        QMessageBox.about(self, title, text)

    def how_to_use(self):
        pass

    def main_menu(self):
        # print(datetime.datetime.now())
        menubar = self.menuBar()
        menubar.addMenu('&File').addAction('Exit',exit)
        menubar.addMenu('&Option')

        about = menubar.addMenu('&Help')
        about.addAction('About', self.about_dev)
        about.addAction('How to use?', self.how_to_use)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
