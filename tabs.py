from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import os
from datetime import datetime
from json import dump
import shutil
import openpyxl
from csv import reader


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.initTabsWidget()
        self.init_tab1()
        self.init_tab2()
        self.init_tab3()
        self.init_tab4()
        self.init_tab5()

    def set_main_fodler(self, text:str) -> None:
        self.path1.setText(text)
        self.main_line1.setText(text)
        self.line_found.setText(text)
        self.line_split_review.setText(text)



    # region tab1
    def init_tab1(self) -> None:
        '''Функция инициализации первого таба.\n'''
        # Create elements
        self.btn1 = QPushButton('Review', self.tab1)
        self.btn1.clicked.connect(lambda : self.main_line1.setText(
                QFileDialog().getExistingDirectory(None,'Select directory')))

        self.btn2 = QPushButton('Run', self.tab1)
        self.btn2.clicked.connect(self.check_elements)
        self.main_line1 = QLineEdit(self.tab1)
        self.line_extension = QLineEdit('.exe',self.tab1)
        self.line_rename_file = QLineEdit('test.txt',self.tab1)
        self.line_rename_file.setToolTip('Only txt files!')
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

    def check_elements(self) -> None:
        '''
        Функция проверки на наличие и корректности введённых данных для вызова определённой операции над файлами.
        '''
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

        self.disabled_check_boxes()

    def disabled_check_boxes(self) -> None:
        '''
        Функция снятия выделения чек-боксов.\n
        Она вызывается при успешной выполенении операции.
        '''
        self.check_box1.setChecked(False)
        self.check_box2.setChecked(False)
        self.check_box3.setChecked(False)

    def convert_bytes(self,size) -> str:
        '''
        Функция определения единиц измерения по размеру удалённых файлов.\n
        Возрвращает единицы измерения и округлённый до целых размер удалённых файлов.
        '''
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0

        return size

    def delete_files(self) -> None:
        '''
        Функция из главного функционала\n
        Одна из функции главного функционала программы.
        Удаляет файлы с определённым расширением или именем.
        '''
        extension = self.line_extension.text()
        size = 0
        count = 0
        self.Print(self.text, 'Start deleting...')
        for root, _, files in os.walk(self.main_line1.text()):
            for file in files:
                if file.endswith(extension):
                    path = os.path.join(root,file)
                    self.Print(self.text, path)
                    size += os.stat(path).st_size
                    os.remove(path)
                    count += 1
        self.Print(self.text, f'Delete {count} files ({self.convert_bytes(size)})')

    def find_first_file(self, endswitch:str, files:list) -> str:
        '''
        Функция выбора первого файла из списка. Файлы ищутся с определённым расширением.
        '''
        for file in files:
            if file.endswith(endswitch):
                return file
        return ''

    def rename_files(self) -> None:
        '''
        Функция из главного функционала\n
        Выполняет поиск файлов с одинаковым именем (например Out_res.txt)
        и переименование по следующем конструкциям:\n
        1.\tназвание папки в которой находится файл + текущее имя + дата и время из найденого dat-файла (если есть хотя бы один в папке);
        2.\tназвание папки в которой находится файл + текущее имя
        '''
        self.Print(self.text,'Start renaming...')
        for root, _, files in os.walk(self.main_line1.text()):
            dat =  self.find_first_file('.dat', files)
            txt =  self.find_first_file(self.line_rename_file.text(), files)
            if not txt: continue
            rename = f'{root.split("/")[-1]}_{txt.split(".")[0]}_{"_".join(dat.split("_")[1:5])}.txt'
            os.rename(f'{root}/{txt}',f'{root}/{rename}')
            self.Print(self.text, f'{root}/{txt} -> {rename}'.replace('\\','/'))

        self.Print(self.text,'End renaming...')

    def delete_empty_directories(self, path:str) -> None:
        '''
        Функция из главного функционала\n
        Выполняет удаление пустых директорий.
        '''
        for _dir in os.listdir(path):
            current_dir = os.path.join(path, _dir)
            if os.path.isdir(current_dir):
                self.delete_empty_directories(current_dir)
                if not os.listdir(current_dir):
                    os.rmdir(current_dir)
                    self.Print(self.text,"Папка удалена: " + current_dir)

    # endregion

    # region tab2

    def init_tab2(self) -> None:
        '''
        Функция инициализации второго таба
        '''
        # Create elements
        self.radio_button1 = QRadioButton('Collect txt', self.tab2)
        self.radio_button2 = QRadioButton('Send out exe', self.tab2)
        self.radio_button1.setChecked(True)
        group = QButtonGroup(self.tab2)
        group.addButton(self.radio_button1)
        group.addButton(self.radio_button2)

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


        grid.addWidget(self.radio_button1, 0,1, alignment=Qt.AlignCenter)
        grid.addWidget(self.radio_button2, 0,3, alignment=Qt.AlignLeft)

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

    def select_second_path(self) -> None:
        '''
        Динамический выбор пути\n
        Учитывает выбор операции (радио кнопки).\n
        Первая операция (выбрано по умолчанию). Сборка txt-файлов требуется два пути:
        1.\tпуть поиска файлов (поиск выполняется и в подпапках по расширению txt)
        2.\tпуть куда они будут помещены\n
        Имеется проблема одинаковых имён файлов в месте хранения, в связи с чем необходимо их переименовывать в момент копирования.
        Новое имя определяется по шаблону "название папки + текущее имя файла"\n
        Вторая операция. Рассылка исполняемых файлов программы обработки, поэтому поля будут содержать следующие параметры:
        1.\tпуть куда куда нужно добавить исполняемый файл (добавляется и в подпапки)
        2.\tпуть к исполняемому файлу, который необходимо разослать
        '''
        if self.radio_button1.isChecked():
            self.path2.setText(
                QFileDialog().getExistingDirectory(None,'Select directory'))
        else:
            self.path2.setText(
                QFileDialog.getOpenFileName(self,'Open File', None, '*.exe')[0])

    def start_move(self) -> None:
        '''
        Функция проверки на наличие и корректности введённых параметров.
        '''
        if not self.path1.text():
            QMessageBox.warning(self, 'Error', 'First path is empty')

        if self.radio_button1.isChecked() and self.path2.text():
            self.collect_files()

        if self.radio_button2.isChecked():
            self.send_out_files()

    def send_out_files(self) -> None:
        '''
        Функция из главного функционала.\n
        Выполняет рассылку исполняемых файлов по папкам.
        '''
        self.Print(self.area, 'Start copy...')
        exe = self.path2.text().split('/')[-1]
        for root,folders,_ in os.walk(self.path1.text()):
            for folder in folders:
                to = os.path.join(root, folder,exe)
                try:
                    shutil.copyfile(self.path2.text(),to)
                    self.Print(self.area, os.path.join(root, folder,exe))
                except shutil.SameFileError:
                    self.Print(self.area, f'File {to} already exists')
        self.Print(self.area, 'Finish copy...')

    def collect_files(self) -> None:
        '''
        Функция из главного функционала.\n
        Выполняет сборку txt-файлов из подпапок в одну папку.
        '''
        self.Print(self.area, 'Start copy...')
        files_list = self.find_files(self.path1.text(),'.txt')
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
        self.Print(self.area, 'Finish copy')

    # endregion

    # region tab3

    def init_tab3(self) -> None:
        '''
        Функция инициализации третьего таба
        '''
        self.line_found = QLineEdit(self.tab3)
        self.line_name_one_to_one = QLineEdit(self.tab3)
        self.line_name_one_to_one.setEnabled(False)
        self.line_name_many_to_one = QLineEdit(self.tab3)
        self.line_name_many_to_one.setEnabled(False)
        self.line_save = QLineEdit(self.tab3)

        self.btn_review_found = QPushButton('Review',self.tab3)
        self.btn_review_found.clicked.connect(lambda : self.line_found.setText(
                QFileDialog().getExistingDirectory(None,'Select directory')))

        self.btn_review_save = QPushButton('Review',self.tab3)
        self.btn_review_save.clicked.connect(lambda : self.line_save.setText(
                QFileDialog().getExistingDirectory(None,'Select directory')))

        self.btn_found = QPushButton('Found',self.tab3)
        self.btn_found.clicked.connect(self.found_files)
        self.btn_save = QPushButton('Save',self.tab3)
        self.btn_save.clicked.connect(self.check_paths)
        self.btn_hide = QPushButton('Hide all', self.tab3)
        self.btn_hide.clicked.connect(self.hide_items)
        self.btn_select = QPushButton('Select all', self.tab3)
        self.btn_select.clicked.connect(self.select_items)

        self.label_select = QLabel(self.tab3)
        self.label_select.setText('Selected: 0 items')

        self.list = QListWidget(self.tab3)
        self.list.setSelectionMode(QAbstractItemView.MultiSelection)



        self.checkbox_xlsx1 = QCheckBox('One file = one sheet',self.tab3)
        self.checkbox_xlsx1.clicked.connect(lambda state: self.line_name_one_to_one.setEnabled(state))
        self.checkbox_xlsx2 = QCheckBox('Many files = one sheet',self.tab3)
        self.checkbox_xlsx2.clicked.connect(lambda state: self.line_name_many_to_one.setEnabled(state))

        grid = QGridLayout()
        grid.addWidget(self.line_found, 0,0,1,2)
        grid.addWidget(self.btn_review_found, 0,2)
        grid.addWidget(self.btn_found, 0,3)
        grid.addWidget(self.checkbox_xlsx1, 1,0)
        grid.addWidget(self.line_name_one_to_one, 1,1)
        grid.addWidget(self.checkbox_xlsx2, 2,0)
        grid.addWidget(self.line_name_many_to_one, 2,1)
        grid.addWidget(self.line_save, 3,0,1,2)
        grid.addWidget(self.btn_review_save, 3,2)

        grid.addWidget(self.btn_hide,4,3)
        grid.addWidget(self.btn_select,4,3, alignment=Qt.AlignTop)

        grid.addWidget(self.label_select, 5,0)

        grid.addWidget(self.list, 4,0,1,3)
        grid.addWidget(self.btn_save, 5,3)
        self.tab3.setLayout(grid)

    def check_paths(self) -> None:
        '''Функция проверки на наличие и корректности введённых параметров.'''
        check1 = self.checkbox_xlsx1.isChecked()
        check2 = self.checkbox_xlsx2.isChecked()

        if not check1 and not check2:
            return QMessageBox.warning(self, 'Error','Choose view xlsx file')

        if not self.line_name_one_to_one.text() and not self.line_name_many_to_one.text():
            return QMessageBox.warning(self, 'Error','Enter the name for xlsx-file')

        if len(self.list.selectedItems()) == 0:
            return QMessageBox.warning(self, 'Error','Choose files for saved')

        if not self.line_save.text():
            return QMessageBox.warning(self, 'Error','Choose folder for saved')


        if check1:
            self.one_file_to_one_sheet()
            QMessageBox.information(self,'Success','Files collected')


        if check2:
            self.many_files_to_one_sheet()
            QMessageBox.information(self,'Success','Files collected')

    def delete_sheet(self,wb):
        '''
        Удаляет лист из эксель файла под именем "Sheet" (Он создаётся по умолчанию).
        '''
        del wb['Sheet']

    def many_files_to_one_sheet(self) -> None:
        '''
        Перебирает txt-файлы, считывая их по строке, и добавляет все строки строки в один лист.
        '''
        _workbook = openpyxl.Workbook()
        _worksheet = _workbook.create_sheet('Excel')
        for item in self.list.selectedItems():
            with open(item.text(),'r') as file:
                cr = reader(file,delimiter = '\t')
                content = [line for line in cr]

                for line in content:
                    for i in range(1, len(line) - 1):
                        line[i] = line[i].replace(' ', '')
                        line[i] = float(line[i])
                    _worksheet.append(line)
                file.close()

        self.delete_sheet(_workbook)
        _workbook.save(filename=os.path.join(self.line_save.text(), self.line_name_many_to_one.text() + '.xlsx'))

    def one_file_to_one_sheet(self) -> None:
        '''Перебирает txt-файлы, считывая их по строке, и добавляет каждый файл в отдельный лист.'''
        _workbook = openpyxl.Workbook()
        for item in self.list.selectedItems():
            _worksheet = _workbook.create_sheet(item.text().split('\\')[-1])
            with open(item.text(),'r') as file:
                cr = reader(file,delimiter = '\t')
                content = [line for line in cr]


                for line in content:
                    for i in range(1, len(line) - 1):
                        line[i] = line[i].replace(' ', '')
                        line[i] = float(line[i])
                    _worksheet.append(line)
                file.close()
            _workbook.save(filename=os.path.join(self.line_save.text(),self.line_name_one_to_one.text() + '.xlsx'))
        self.delete_sheet(_workbook)

    def found_files(self) -> None:
        '''
        Функция поиска txt-файлов. Все текстовые документы (.txt) которые находит, добавляет в лист для выбора необходимых файлов перевода в эксель.
        '''
        self.list.clear()
        result = []
        if not self.line_found.text():
            return result
        self.list.addItems(self.find_files(self.line_found.text(), '.txt'))
        self.list.itemClicked.connect(self.item_clicked)

    def changeItems(self, flag) -> None:
        '''Изменияет состояние элемента.'''
        for item in range(self.list.count()):
            self.list.item(item).setSelected(flag)
        self.item_clicked()

    def select_items(self) -> None:
        '''Выделяет все элементы'''
        return self.changeItems(True)

    def hide_items(self) -> None:
        '''Снимает все выделения'''
        return self.changeItems(False)

    def item_clicked(self) -> None:
        '''Изменяет лэйбл при выделении элемента. Показывает сколько элементов выбрано.'''
        return self.label_select.setText(f'Selected: {len(self.list.selectedItems())} items')

    # endregion

    # region tab4

    def init_tab4(self) -> None:
        '''Функция инициализации четвертого таба.\n'''
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

    def generate_config_file(self) -> None:
        '''Генерирует файл конфигурации для программы обработки'''
        Radar = self.group1.checkedButton()     #Радар
        Mode = self.group2.checkedButton()      #Режим
        Channel = self.group3.checkedButton()   #Канал

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

    # region tab5

    def init_tab5(self) -> None:
        '''Функция инициализации пятого таба.\n'''
        self.radio_optimization = QRadioButton('Splitting to optimize processing', self.tab5)
        self.radio_profile = QRadioButton('Splitting by profiles')

        self.radio_optimization.setChecked(True)

        self.line_split_review = QLineEdit(self.tab5)
        self.line_first_file = QLineEdit(self.tab5)
        self.line_first_file.setToolTip('First file')
        self.line_last_file = QLineEdit(self.tab5)
        self.line_last_file.setToolTip('Last file')
        self.line_profile_name = QLineEdit(self.tab5)
        self.line_profile_name.setToolTip('Name profile')

        self.area_split = QTextEdit(self.tab5)
        self.area_split.setReadOnly(True)

        self.radio_optimization.clicked.connect(self.optimizate_radio_elements)
        self.radio_profile.clicked.connect(self.profile_radio_elements)

        self.btn_split_review = QPushButton('Review', self.tab5)
        self.btn_split_review.clicked.connect(lambda : self.line_split_review.setText(
                QFileDialog().getExistingDirectory(None,'Select directory')))

        self.btn_split = QPushButton('Run', self.tab5)
        self.btn_split.clicked.connect(self.checked_elements)
        self.combo = QComboBox(self.tab5)
        self.combo.addItems(['2','3','4','5','6','7','8','9','10'])

        self.optimizate_radio_elements()
        group = QButtonGroup(self.tab5)
        group.addButton(self.radio_optimization)
        group.addButton(self.radio_profile)


        grid = QGridLayout()
        grid.addWidget(QLabel('Path'), 0,0)
        grid.addWidget(self.line_split_review, 0,1,1,4)
        grid.addWidget(self.btn_split_review, 0,5)
        grid.addWidget(self.radio_optimization, 1,0)
        grid.addWidget(self.combo, 1,1, alignment=Qt.AlignLeft)
        grid.addWidget(self.radio_profile, 2,0)
        grid.addWidget(self.line_first_file, 2,1)
        grid.addWidget(self.line_last_file, 2,2)
        grid.addWidget(self.line_profile_name, 2,3)
        grid.addWidget(self.area_split, 3,0,3,6)
        grid.addWidget(self.btn_split, 7,5)
        self.tab5.setLayout(grid)

    def optimizate_radio_elements(self) -> None:
        '''Включает комбо-бокс и отключает три линии редактирования.'''
        self.combo.setDisabled(False)
        self.line_first_file.setDisabled(True)
        self.line_last_file.setDisabled(True)
        self.line_profile_name.setDisabled(True)

    def profile_radio_elements(self) -> None:
        '''Отключает комбо-бокс и включает три линии редактирования.'''
        self.combo.setDisabled(True)
        self.line_first_file.setDisabled(False)
        self.line_last_file.setDisabled(False)
        self.line_profile_name.setDisabled(False)

    def checked_elements(self) -> None:
        '''Функция проверки на наличие и корректности введённых параметров.'''
        if self.radio_optimization.isChecked():
            self.optimization()

        if self.radio_profile.isChecked() and self.create_profile_folder():
            self.copy_files(self.profiles())
            self.Print(self.area_split, self.line_profile_name.text() + ' is done!')

    def get_files(self) -> list[str]:
        '''Возвращает список dat-файлов найденных в указанной директории.'''
        cwd = self.line_split_review.text()
        return [os.path.join(cwd,item) for item in os.listdir(cwd) if item.endswith('.dat')]

    def copy_files(self, files) -> None:
        '''Копирует список файлов в указанную папку'''
        for item in files:
            try:
                shutil.copyfile(item,os.path.join(self.profile_folder,item.split('\\')[-1]))
            except Exception as ex:
                self.Print(self.area_split, ex)

    def create_profile_folder(self) -> bool:
        '''Создает папку для профиля и содержит список файлов по профилю.\n
        Возвращает:\n
        1.\tTrue  - папка успешно создана;
        2.\tFalse - папка с таким именем уже существует.
        '''
        self.profile_folder = os.path.join(self.line_split_review.text(), self.line_profile_name.text())
        if os.path.isdir(self.profile_folder):
            QMessageBox.warning(self, 'Error', 'Folder already exists')
            return False
        os.makedirs(self.profile_folder)
        return True

    def profiles(self) -> list:
        '''Возвращает список файлов, которые входят в профиль.'''
        files = self.get_files()
        res = []
        for item in range(len(files)):
            if files[item].endswith(self.line_first_file.text() + '.dat'):
                i = item
                while(not files[i].endswith(self.line_last_file.text() + '.dat')):
                    res.append(files[i])
                    i += 1
                res.append(files[i])

        return res

    def optimization(self) -> None:
        '''Разбивает файлы по количеству(QComboBox) указанных папок.'''
        split_num = int(self.combo.currentText())
        self.split_num = split_num
        folders = self.make_directories()
        dat_files = self.get_files()
        # поиск файлов dat
        count_dat_files = len(dat_files)
        split_list = [count_dat_files // split_num] * split_num
        split_list[-1] += count_dat_files % split_num
        for i in range(split_num):
            for _ in range(split_list[i]):
                try:
                    shutil.move(dat_files[0],os.path.join(folders[i],dat_files[0].replace('\\','/').split('/')[-1]))
                    dat_files.pop(0)
                except FileNotFoundError:
                    self.Print(self.area_split, 'File Not Found Error')

    def make_directories(self) -> list[str]:
        '''Возрващает список созданных директорий.'''
        cwd = self.line_split_review.text()
        folders = []
        for i in range(self.split_num):
            try:
                folder = os.path.join(cwd,f'Path_{i+1}')
                folders.append(folder)
                os.makedirs(folder)
            except FileExistsError:
                self.Print(self.area_split, f'Folder {folder} already exists')
                continue

        self.Print(self.area_split,f'Folders successfull created')
        return folders

    # endregion

    def initTabsWidget(self) -> None:
        '''
        Функция инициализации табов
        '''
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(300,200)

        self.tabs.addTab(self.tab1,"Clean up")
        self.tabs.addTab(self.tab2,"Move files")
        self.tabs.addTab(self.tab3,"Txt to xlsx")
        self.tabs.addTab(self.tab4,"Config file")
        self.tabs.addTab(self.tab5,"Split files")

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)
        self.setLayout(vbox)

    def find_files(self, cwd:str, extension:str) -> list[str]:
        '''
        Функция поиска файлов по расширению.\n
        Возрващает список строк.\n
        Одна строка - это полный путь к файлу.
        '''
        files_list = []
        for root, _, files in os.walk(cwd):
            for item in files:
                if item.endswith(extension):
                    files_list.append(os.path.join(root,item))
        return files_list

    def Print(self,textEdit,string:str) -> None:
        '''
        Функция печати результата.\n
        Принимает объект, в котором будет отображена строка, которая передаётся третьим параметром
        '''
        textEdit.append(f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {string}')
