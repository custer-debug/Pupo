import sys
from PyQt5.QtWidgets import QShortcut,QMenu,QMainWindow,QMessageBox,QApplication,QFileDialog
from PyQt5.QtGui import QIcon, QKeySequence
import os
from tabsDraw import TableWidget
from platform import platform
from json import load, dump

light_theme_default = '''

QPushButton{
    padding : 8px 20px;
}
QLineEdit{
    height: 27px;
}
QProgressBar{
    height: 25px;
}
QMenuBar{
    background-color: lightgray;
}
QTabBar::tab {
    padding: 8px;
}
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,300, 900,600)
        self.setObjectName('MainWindow')
        self.setWindowIcon(QIcon('./config/icons/ssd_icon.png'))
        self.setWindowTitle("pupo")
        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.pathSettings = 'config\settings.json'
        if not os.path.exists(self.pathSettings):
            self.create_settings_file()
        else:
            self.get_settings()
        try:
            self.setStyleSheet(open(self.settings['theme']).read())
        except FileNotFoundError:
            self.setStyleSheet(light_theme_default)
        self.table_widget.set_main_fodler(self.settings['prev_folders'][self.count_])
        self.main_menu()

    def increase_counter(self,length) -> None:
        '''Изменение счетчика который используется для сохранения или получения предыдущих директорий.\n
        settings['prev_folders'][self.count_]'''
        if self.count_ < length - 1:
            self.count_ += 1
        else:
            self.count_ = 0

    def select_folder(self) -> str:
        '''Выбор главной директории.
        Она сразу будет записана в несколько полей редактирования.'''
        folder = QFileDialog().getExistingDirectory(
                None, "Select folder")
        if not folder:
            cwd = os.getcwd().replace('\\','/')
            self.table_widget.set_main_fodler(cwd)
            return cwd
        else:
            self.table_widget.set_main_fodler(folder)
            return folder

    def get_main_folder(self) -> None:
        '''Запись главной директории в словарь для дальнейшего
        сохранение в файл настроек (settings.json).'''
        if not self.settings['prev_folders']:
            self.settings['prev_folders'] = self.select_folder()

        elif type(self.settings['prev_folders']) == str:
            tmp = []
            tmp.append(self.settings['prev_folders'])
            tmp.append(self.select_folder())
            self.settings['prev_folders'] = tmp

        elif type(self.settings['prev_folders'] == list):
            if len(self.settings['prev_folders']) <= 5:
                self.settings['prev_folders'][self.count_] = self.select_folder()
                self.increase_counter(len(self.settings['prev_folders']))
                self.settings['count_folder'] = self.count_ - 1
            else:
                self.settings['prev_folders'].append(self.select_folder())

        self.set_settings()

    def clear_main_folder(self) -> None:
        '''Очищение полей редактирования.'''
        self.table_widget.set_main_fodler('')

    def msg_box_about(self) -> None:
        '''Вывод окна "О программе".'''
        title = 'О программе'
        text = f'''
        Programm to Use Program Operations (Pupo)
        Version: 2.1.0
        Update: 2021-12-09 16:40:02
        OS: {platform()} 64-bit
        @Scientific and Production Association RadioSignal JSC
        Software engineers: Krekoten Roman, Nenarokomov Maxim
        '''
        return QMessageBox.about(self, title, text)

    def set_settings(self) -> None:
        '''Запись настроек в файл settings.json.'''
        with open(self.pathSettings, 'w') as json:
            dump(self.settings, json, indent=4)

    def get_settings(self) -> None:
        '''Получение настроек из файла settings.json.'''
        with open(self.pathSettings, 'r') as json:
            self.settings = load(json)
        self.count_ = self.settings['count_folder']

    def create_settings_file(self) -> None:
        '''Если файла настроек нет, в этой функции он создастся.'''
        self.settings = {
            'count_folder':0,
            'prev_folders':[os.getcwd().replace('\\','/')],
            'theme':'./config/themes/light_theme.css'
        }
        self.count_ = 0
        try:
            os.mkdir(os.path.join(os.getcwd(),'config/'))
            with open(self.pathSettings, 'w+') as f:
                dump(self.settings, f, indent=4)
        except Exception as ex:
            print(ex)



    def set_prevension_folder(self) -> None:
        '''Добавление сохранённой директории в линии редактирования.'''
        return self.table_widget.set_main_fodler(self.sender().objectName())

    def msg_restart_program(self) -> None:
        '''Сообщение'''
        return QMessageBox.information(self,'Сообщение','Перезапустите программу')

    def light_theme(self) -> None:
        '''Сохранение светлой темы в файл настроек (settings.json).'''
        self.settings['theme'] = './config/themes/light_theme.css'
        self.set_settings()
        self.msg_restart_program()

    def dark_theme(self) -> None:
        '''Сохранение темной темы в файл настроек (settings.json).'''
        self.settings['theme'] = './config/themes/dark_theme.css'
        self.set_settings()
        self.msg_restart_program()

    def menu_file(self) -> None:
        '''Функция обработки секции "file" в меню программы.'''
        fileMenu = QMenu('&Файл',self)
        self.menubar.addMenu(fileMenu)
        fileMenu.addAction('Открыть папку\tCtrl+O',self.get_main_folder)
        fileMenu.addAction('Очистить \tCtrl+I',self.clear_main_folder)
        fileMenu.addSeparator()
        QShortcut(QKeySequence('Ctrl+O'),self).activated.connect(self.get_main_folder)
        QShortcut(QKeySequence('Ctrl+I'),self).activated.connect(self.clear_main_folder)
        if type(self.settings['prev_folders']) == list:
            for folder in self.settings['prev_folders']:
                tmp = fileMenu.addAction(folder,self.set_prevension_folder)
                tmp.setObjectName(folder)


            fileMenu.addSeparator()
        elif type(self.settings['prev_folders']) == str:
            fileMenu.addAction(self.settings['prev_folders'])

        fileMenu.addAction('Выход',sys.exit)

    def menu_option(self) -> None:
        '''Функция обработки секции "Option" в меню программы.'''
        if os.path.exists('./config/themes/dark_theme.css'):
            option = self.menubar.addMenu('&Опции')
            option.addAction('Светлая тема', self.light_theme)
            option.addAction('Темная тема', self.dark_theme)

    def menu_about(self) -> None:
        '''Функция обработки секции "About" в меню программы.'''
        about = self.menubar.addMenu('&Помощь')
        about.addAction('О программе', self.msg_box_about)

    def reference_window(self) -> None:
        '''Вывод окна справки.'''
        return QMessageBox.information(self, 'Справка',
            open(self.settings['reference'], 'r', encoding='utf-8').read())


    # try:
    # about.addAction('Справка', self.reference_window)
    # except Exception as e:
    # print(e)

    def main_menu(self) -> None:
        '''Функция инициализации меню программы и добавление в него секции.'''
        self.menubar = self.menuBar()
        self.menu_file()
        self.menu_option()
        self.menu_about()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
