from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import os
from datetime import date, datetime
from json import dump
import shutil

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initTabsWidget()
        self.init_tab1()
        self.init_tab2()
        self.init_tab3()
        self.init_tab4()

    # region tab1
    def init_tab1(self):
        # Create elements
        self.btn1 = QPushButton('Review', self.tab1)
        self.btn1.clicked.connect(lambda : self.main_line1.setText(
                QFileDialog().getExistingDirectory(None,'Select directory')))

        self.btn2 = QPushButton('Run', self.tab1)
        self.btn2.clicked.connect(self.check_elements)
        self.main_line1 = QLineEdit(self.tab1)
        self.line_extension = QLineEdit('.exe',self.tab1)
        self.line_rename_file = QLineEdit('test.txt',self.tab1)
        self.line_extension.setEnabled(False)
        self.line_rename_file.setEnabled(False)

        self.check_box1 = QCheckBox('Delete files', self.tab1)
        self.check_box2 = QCheckBox('Rename files', self.tab1)
        self.check_box3 = QCheckBox('Delete empty dir', self.tab1)
        self.check_box1.clicked.connect(lambda state: self.line_extension.setEnabled(state))
        self.check_box2.clicked.connect(lambda state: self.line_rename_file.setEnabled(state))

        self.text = QTextEdit(self.tab1)
        self.text.setReadOnly(True)

        # Create grid
        grid = QGridLayout()
        grid.addWidget(self.main_line1, 0, 0,1,6)
        grid.addWidget(self.btn1, 0, 6)
        grid.addWidget(self.check_box1, 1,0)
        grid.addWidget(self.line_extension,1,1, alignment=Qt.AlignCenter)
        grid.addWidget(self.check_box2, 2,0)
        grid.addWidget(self.line_rename_file, 2,1, alignment=Qt.AlignCenter)
        grid.addWidget(self.check_box3, 3,0)
        grid.addWidget(self.text, 4,0,5,7)
        grid.addWidget(self.btn2, 10, 6)

        self.tab1.setLayout(grid)

    def check_elements(self):
        self.text.clear()
        if not os.path.exists(self.main_line1.text()):
            QMessageBox.warning(self, 'Error', 'Path is not exists')
            return

        if self.check_box1.isChecked() and self.line_extension.text():
            self.delete_files()
        if self.check_box2.isChecked() and self.line_rename_file.text():
            self.rename_files()
        if self.check_box3.isChecked():
            self.delete_empty_directories(self.main_line1.text())

        if not (self.check_box1.isChecked() or self.check_box2.isChecked() or self.check_box3.isChecked()):
            QMessageBox.warning(self, 'Error', 'Choose action')


    def convert_bytes(self,size):
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0

        return size


    def delete_files(self):
        extension = self.line_extension.text()
        size = 0
        count = 0
        self.Print(self.text, 'Start deleting...')
        for root, _, files in os.walk(self.main_line1.text()):
            for file in files:
                if file.endswith(extension):
                    path = os.path.join(root,file)
                    self.Print(self.text, path)
                    # os.remove(path)
                    size += os.stat(path).st_size
                    count += 1
        self.Print(self.text, f'Delete {count} files ({self.convert_bytes(size)})')




    def find_first_file(self, endswitch:str, files:list) -> str:
        for file in files:
            if file.endswith(endswitch):
                return file
        return ''



    def rename_files(self) -> None:
        self.Print(self.text,'Start renaming...')
        for root, _, files in os.walk(self.main_line1.text()):
            dat =  self.find_first_file('.dat', files)
            txt =  self.find_first_file(self.line_rename_file.text(), files)
            if not txt: continue
            rename = f'{root.split("/")[-1]}_{txt.split(".")[0]}_{"_".join(dat.split("_")[1:5])}.txt'
            os.rename(f'{root}/{txt}',f'{root}/{rename}')
            self.Print(f'{root}/{txt} -> {rename}'.replace('\\','/'))

        self.Print(self.text,'End renaming...')



    def delete_empty_directories(self, path:str) -> None:
        for _dir in os.listdir(path):
            current_dir = os.path.join(path, _dir)
            if os.path.isdir(current_dir):
                self.delete_empty_directories(current_dir)
                if not os.listdir(current_dir):
                    os.rmdir(current_dir)
                    self.Print(self.text,"Папка удалена: " + current_dir)

    # endregion


    def init_tab2(self):
        # Create elements
        self.radio_button1 = QRadioButton('Collect txt', self.tab2)
        self.radio_button2 = QRadioButton('Split dat', self.tab2)
        self.radio_button3 = QRadioButton('Send out exe', self.tab2)
        self.radio_button1.setChecked(True)
        self.radio_button1.clicked.connect(self.show_elements)
        self.radio_button2.clicked.connect(self.hide_elements)
        self.radio_button3.clicked.connect(self.show_elements)
        group = QButtonGroup(self.tab2)
        group.addButton(self.radio_button1)
        group.addButton(self.radio_button2)
        group.addButton(self.radio_button3)


        self.label_1 = QLabel('Path', self.tab2)
        self.label_2 = QLabel('Path', self.tab2)

        self.path1 = QLineEdit(self.tab2)
        self.path2 = QLineEdit(self.tab2)
        self.area = QTextEdit(self.tab2)
        self.area.setReadOnly(True)
        self.probar = QProgressBar(self.tab2)
        self.probar.setAlignment(Qt.AlignCenter)

        self.btn1 = QPushButton('Review',self.tab2)
        self.btn2 = QPushButton('Review',self.tab2)
        self.btn1.clicked.connect(lambda : self.path1.setText(
                QFileDialog().getExistingDirectory(None,'Select directory')))
        self.btn2.clicked.connect(self.select_second_path)

        self.btn4 = QPushButton('Run',self.tab2)
        self.btn4.clicked.connect(self.start_move)
        # Create grid for paint elements
        grid = QGridLayout()
        grid.setVerticalSpacing(30)
        grid.setRowStretch(6,2)
        grid.setColumnStretch(0,1)
        grid.setColumnStretch(1,5)
        grid.setColumnStretch(2,5)
        grid.setColumnStretch(3,5)


        grid.addWidget(self.radio_button1, 0,1, alignment=Qt.AlignLeft)
        grid.addWidget(self.radio_button2, 0,2, alignment=Qt.AlignCenter)
        grid.addWidget(self.radio_button3, 0,3, alignment=Qt.AlignRight)

        grid.addWidget(self.label_1, 1,0)
        grid.addWidget(self.label_2, 2,0)

        grid.addWidget(self.path1, 1,1,1,3)
        grid.addWidget(self.path2, 2,1,1,3)
        grid.addWidget(self.area, 3,1,3,3)
        grid.addWidget(self.probar, 6, 1, 1, 3)

        grid.addWidget(self.btn1, 1, 4, 1,1)
        grid.addWidget(self.btn2, 2, 4, 1,1)
        grid.addWidget(self.btn4, 6, 4, 1,1, alignment=Qt.AlignBottom)

        self.tab2.setLayout(grid)


    def hide_elements(self) -> None:
        self.path2.setText('')
        self.path2.setDisabled(True)
        self.btn2.setDisabled(True)

    def show_elements(self) -> None:
        self.path2.setText('')
        self.path2.setDisabled(False)
        self.btn2.setDisabled(False)


    def select_second_path(self):
        if self.radio_button1.isChecked():
            self.path2.setText(
                QFileDialog().getExistingDirectory(None,'Select directory'))
        else:
            self.path2.setText(
                QFileDialog.getOpenFileName(self,'Open File', None, '*.exe')[0])



    def start_move(self):
        if not self.path1.text():
            QMessageBox.warning(self, 'Error', 'First path is empty')

        if self.radio_button1.isChecked() and self.path2.text():
            self.collect_files()

        if self.radio_button2.isChecked():
            self.cpu_count = os.cpu_count()
            self.split_files()

        if self.radio_button3.isChecked():
            print('send out exe')


    def collect_files(self) -> None:
        self.Print(self.area, 'Start copy...')
        files_list = self.find_files(self.path1.text())
        size = len(files_list)
        for item in files_list:
            split = item.replace('\\','/').split('/')
            rename = f'{split[-2]}_{split[-1]}'
            to_path = os.path.join(self.path2.text(),rename)
            shutil.copyfile(item,to_path)
            percents = int((files_list.index(item)+1) / len(files_list)) * 100
            self.probar.setValue(percents)
            self.Print(self.area, f'{item} -> {to_path}')
        self.Print(self.area, f'{size} files copied')
        self.Print(self.area, 'End copy')


    def split_files(self):
        folders = self.make_directories()
        cwd = self.path1.text()
        files = os.listdir(cwd)
        # поиск файлов dat
        dat_files = [os.path.join(cwd,item) for item in files if item.endswith('.dat')]
        count_dat_files = len(dat_files)
        split_list = [count_dat_files // self.cpu_count] * self.cpu_count
        split_list[-1] += count_dat_files % self.cpu_count
        for i in range(self.cpu_count):
            for _ in range(split_list[i]):
                try:
                    shutil.move(dat_files[0],os.path.join(folders[i],dat_files[0].replace('\\','/').split('/')[-1]))
                    dat_files.pop(0)
                except FileNotFoundError:
                    self.Print(self.area, 'File Not Found Error')


    def make_directories(self) -> list[str]:
        cwd = self.path1.text()
        folders = []
        for i in range(self.cpu_count):
            try:
                folder = os.path.join(cwd,f'Path_{i+1}')
                folders.append(folder)
                os.makedirs(folder)
            except FileExistsError:
                self.Print(self.area, f'Folder {folder} already exists')
                continue

        self.Print(self.area,f'Folders successfull created')
        return folders




    # region tab3


    def init_tab3(self):
        self.line_found = QLineEdit(self.tab3)
        self.line_save1 = QLineEdit(self.tab3)
        self.line_save1.setEnabled(False)
        self.line_save2 = QLineEdit(self.tab3)
        self.line_save2.setEnabled(False)

        self.btn_review = QPushButton('Review',self.tab3)
        self.btn_review.clicked.connect(lambda : self.line_found.setText(
                QFileDialog().getExistingDirectory(None,'Select directory')))

        self.btn_found = QPushButton('Found',self.tab3)
        self.btn_save = QPushButton('Save',self.tab3)
        self.btn_hide = QPushButton('Hide all', self.tab3)
        self.btn_hide.clicked.connect(self.hide_items)
        self.btn_select = QPushButton('Select all', self.tab3)
        self.btn_select.clicked.connect(self.select_items)

        self.label_select = QLabel(self.tab3)
        self.label_select.setText('Selected: 0 items')

        self.list = QListWidget(self.tab3)
        self.list.setSelectionMode(QAbstractItemView.MultiSelection)
        l = ['One','Two', 'Three', 'Four', 'Five']
        self.list.addItems(l)
        self.list.itemClicked.connect(self.item_clicked)

        self.checkbox_xlsx1 = QCheckBox('One file = one sheet',self.tab3)
        self.checkbox_xlsx1.clicked.connect(lambda state: self.line_save1.setEnabled(state))
        self.checkbox_xlsx2 = QCheckBox('Many files = one sheet',self.tab3)
        self.checkbox_xlsx2.clicked.connect(lambda state: self.line_save2.setEnabled(state))

        grid = QGridLayout()
        grid.addWidget(self.line_found, 0,0,1,2)
        grid.addWidget(self.btn_review, 0,2)
        grid.addWidget(self.btn_found, 0,3)
        grid.addWidget(self.checkbox_xlsx1, 1,0)
        grid.addWidget(self.line_save1, 1,1)
        grid.addWidget(self.checkbox_xlsx2, 2,0)
        grid.addWidget(self.line_save2, 2,1)
        grid.addWidget(self.btn_hide,3,3)
        grid.addWidget(self.btn_select,3,3, alignment=Qt.AlignTop)

        grid.addWidget(self.label_select, 4,0)

        grid.addWidget(self.list, 3,0,1,3)
        grid.addWidget(self.btn_save, 4,3)
        self.tab3.setLayout(grid)


    def changeItems(self, flag) -> None:
        for item in range(self.list.count()):
            self.list.item(item).setSelected(flag)
        self.item_clicked()

    def select_items(self) -> None:
        return self.changeItems(True)

    def hide_items(self) -> None:
        return self.changeItems(False)

    def item_clicked(self) -> None:
        return self.label_select.setText(f'Selected: {len(self.list.selectedItems())} items')

    # endregion

    # region tab4

    def init_tab4(self) -> None:
        # Create elements
        self.radio_config1 = QRadioButton('1200', self.tab4)
        self.radio_config2 = QRadioButton('2500', self.tab4)
        self.radio_config3 = QRadioButton('Local', self.tab4)
        self.radio_config4 = QRadioButton('Reson', self.tab4)
        self.radio_config5 = QRadioButton('2', self.tab4)
        self.radio_config6 = QRadioButton('4', self.tab4)

        self.group1 = QButtonGroup(self.tab4)
        self.group1.addButton(self.radio_config1)
        self.group1.addButton(self.radio_config2)

        self.group2 = QButtonGroup(self.tab4)
        self.group2.addButton(self.radio_config3)
        self.group2.addButton(self.radio_config4)

        self.group3 = QButtonGroup(self.tab4)
        self.group3.addButton(self.radio_config5)
        self.group3.addButton(self.radio_config6)

        self.save_json_btn = QPushButton('Save',self.tab4)
        self.save_json_btn.clicked.connect(self.generate_config_file)

        grid = QGridLayout()
        grid.addWidget(QLabel('Radar'), 0,0)
        grid.addWidget(self.radio_config1, 0,1)
        grid.addWidget(self.radio_config2, 0,2)
        grid.addWidget(QLabel('Mode'), 1,0)
        grid.addWidget(self.radio_config3, 1,1)
        grid.addWidget(self.radio_config4, 1,2)
        grid.addWidget(QLabel('Channel'), 2,0)
        grid.addWidget(self.radio_config5, 2,1)
        grid.addWidget(self.radio_config6, 2,2)
        grid.addWidget(self.save_json_btn, 3,2, alignment=Qt.AlignCenter)
        grid.setRowStretch(4,2)
        grid.setVerticalSpacing(20)

        self.tab4.setLayout(grid)




    def generate_config_file(self):

        Radar = self.group1.checkedButton()
        Mode = self.group2.checkedButton()
        Channel = self.group3.checkedButton()

        if Radar == None or Mode == None or Channel == None:
            return

        _dict = {
            'Radar':Radar.text(),
            'Mode':Mode.text(),
            'Channel':Channel.text()

        }

        with open('config.json', 'w') as json:
            dump(_dict,json,indent=4)

        QMessageBox.information(self, 'Success', 'File successful saved')

    # endregion


    def initTabsWidget(self) -> None:

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300,200)

        self.tabs.addTab(self.tab2,"Move files")
        self.tabs.addTab(self.tab1,"Clean up")
        self.tabs.addTab(self.tab3,"Txt to xlsx")
        self.tabs.addTab(self.tab4,"Config file")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)
        self.setLayout(vbox)
        # self.area.Print('hello')


    def find_files(self, cwd:str) -> list[str]:
        files_list = []
        for root, _, files in os.walk(cwd):
            for file in files:
                if file.endswith('.txt'):
                    files_list.append(f'{root}/{file}')
        return files_list

    def Print(self,textEdit,string:str) -> None:
        textEdit.append(f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {string}')
