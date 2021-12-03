import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
from os import getcwd, execl,path
import tabs
from platform import platform
from json import load, dump


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(500,300, 900,600)
        self.setObjectName('MainWindow')
        pixmapi = getattr(QStyle, 'SP_FileDialogNewFolder')
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.setWindowTitle("pupo")
        self.table_widget = tabs.MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.get_settings()
        self.setStyleSheet(open(self.settings['theme']).read())
        self.table_widget.set_main_fodler(self.settings['prev_folders'][self.count_])
        self.main_menu()

    def increase_counter(self,length):
        if self.count_ == length:
            self.count_ = 0
        else:
            self.count_ += 1

    def select_folder(self) -> str:
        folder = QFileDialog().getExistingDirectory(
                None, "Select folder")
        if not folder:
            cwd = getcwd().replace('\\','/')
            self.table_widget.set_main_fodler(cwd)
            return cwd
        else:
            self.table_widget.set_main_fodler(folder)
            return folder

    def get_main_folder(self):
        if not self.settings['prev_folders']:
            self.settings['prev_folders'] = self.select_folder()

        elif type(self.settings['prev_folders']) == str:
            tmp = []
            tmp.append(self.settings['prev_folders'])
            tmp.append(self.select_folder())
            self.settings['prev_folders'] = tmp

        elif type(self.settings['prev_folders'] == list):
            if len(self.settings['prev_folders']) >= 5:
                self.settings['prev_folders'][self.count_] = self.select_folder()
                self.increase_counter(len(self.settings['prev_folders']))
                self.settings['count_folder'] = self.count_
            else:
                self.settings['prev_folders'].append(self.select_folder())

        self.set_settings()


    def clear_main_folder(self):
        self.table_widget.set_main_fodler('')


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


    def set_settings(self) -> None:
        with open('settings.json', 'w') as json:
            dump(self.settings, json, indent=4)



    def get_settings(self) -> None:
        with open('settings.json', 'r') as json:
            self.settings = load(json)
        self.count_ = self.settings['count_folder']

    def how_to_use(self):
        pass

    def prev_folders(self):
        self.table_widget.set_main_fodler(self.sender().objectName())

    def menu_file(self):
        fileMenu = QMenu('&File',self)
        self.menubar.addMenu(fileMenu)
        fileMenu.addAction('Open folder\tCtrl+O',self.get_main_folder)
        fileMenu.addAction('Clear \tCtrl+I',self.clear_main_folder)
        fileMenu.addSeparator()
        QShortcut(QKeySequence('Ctrl+O'),self).activated.connect(self.get_main_folder)
        QShortcut(QKeySequence('Ctrl+I'),self).activated.connect(self.clear_main_folder)
        if type(self.settings['prev_folders']) == list:
            for folder in self.settings['prev_folders']:
                tmp = fileMenu.addAction(folder,self.prev_folders)
                tmp.setObjectName(folder)


            fileMenu.addSeparator()
        elif type(self.settings['prev_folders']) == str:
            fileMenu.addAction(self.settings['prev_folders'])

        fileMenu.addAction('Exit',exit)


    def light_theme(self):
        self.settings['theme'] = './themes/light_theme.css'
        self.set_settings()
        execl(sys.executable,path.abspath(__file__),*sys.argv)

    def dark_theme(self):
        self.settings['theme'] = './themes/dark_theme.css'
        self.set_settings()
        execl(sys.executable,path.abspath(__file__),*sys.argv)


    def menu_option(self):
        option = self.menubar.addMenu('&Option')
        option.addAction('light theme', self.light_theme)
        option.addAction('Dark theme', self.dark_theme)


    def menu_about(self):
        about = self.menubar.addMenu('&Help')
        about.addAction('About', self.about_dev)
        about.addAction('How to use?', self.how_to_use)


    def main_menu(self):
        self.menubar = self.menuBar()
        self.menu_file()
        self.menu_option()
        self.menu_about()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
