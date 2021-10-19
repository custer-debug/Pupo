from typing import List, Match
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from DefaultVariable import *
import os
import shutil
from Function import * 

class CopyWindowClass(QMainWindow):
    log_update = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.first_path = ''
        self.second_path = ''
        self.third_path = ''
        self.log_txt = ''
        self.radio_bool = False
        self.default_variable()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()


    def default_variable(self):
        self.setGeometry(ax,ay,aw,ah)
        self.label_handle()
        self.radio_button_handle()
        self.line_edit_handle()
        self.button_handle()
        self.checkbox_handle_function()

 
    def checkbox_handle_function(self):
        self.checkbox = create_check_box(self, "Txt to xslx", 160)

  
    def label_handle(self):
        self.first_label = create_label_function(self,label_from, y1)
        self.second_label = create_label_function(self, label_to, y2)
        self.third_label = create_label_function(self, "Json: ", y2 + 60)
        self.third_label.hide()

    def show_elements(self):
        # print('show')
        self.checkbox.hide()
        self.third_line_edit.show()
        self.third_label.show()
        self.button_review.show()

    def hide_elements(self):
        # print('hide')
        self.button_review.hide()
        self.checkbox.show()
        self.third_line_edit.hide()
        self.third_label.hide()

    def change_elements_option_function(self,title, first_label, second_label,height, btn_y,check_box):
        self.radio_bool = check_box
        self.setWindowTitle(title)
        self.first_label.setText(first_label)
        self.second_label.setText(second_label)
        self.setGeometry(ax,ay,aw,height)
        self.button_run.move(xb,btn_y)

        self.difference_func(
            check_box,
            self.hide_elements,
            self.show_elements, 
            self.show_elements
        )


    def difference_func(self,argc, function_1,function_2,function_3):
        match argc:
            case '.txt':
                return function_1()
            case '.dat':
                return function_2()
            case '.exe':
                return function_3()


    def difference_args(self, arg:str, function, args1 = [], args2 = [], args3 = [] ):
        match arg:
            case '.txt':
                return function(*args1)
            case '.dat':
                return function(*args2)
            case '.exe':
                return function(*args3)


    def radio_button_checked_function(self, button):
        self.difference_args(
            button.text(),
            self.change_elements_option_function,
            [copy_files, label_from, label_to,ah,yb3, txt],
            [name_split, label_Path, label_exe,260,yb3 + 60, dat],
            ['Copy exe+json', label_Path, label_exe,260,yb3 + 60, exe]
        )


    def check_radio_buttons(self):
        if not self.check_paths(): return

        self.difference_args(self.difference_func(
            self.radio_bool,
            self.collect_files,
            self.move_dat_files,
            self.send_out_file
        ),
        success,
        [self, SuccessCopyFiles],
        [self, SplitSucces],
        [self, 'Файл перемещен'] 
        )



    def radio_button_handle(self):
        self.radio_txt = radio_button_create(self, txt,xr1, yr)
        self.radio_dat = radio_button_create(self, dat,xr2, yr)
        self.radio_exe = radio_button_create(self, exe,xr3, yr)
        self.radio_txt.setChecked(True)

        group = QButtonGroup(self)
        group.addButton(self.radio_txt)
        group.addButton(self.radio_dat)
        group.addButton(self.radio_exe)
        group.buttonClicked.connect(self.radio_button_checked_function)



    def line_edit_handle(self):
        self.first_line_edit = create_line_edit(self, xledit, yledit_1, wl)
        self.second_line_edit = create_line_edit(self, xledit, yledit_2, wl)
        self.third_line_edit = create_line_edit(self, xledit, yledit_2 + 60, wl)
        self.third_line_edit.hide()
        

    def button_handle(self):
        create_button(self, review, xb, yb1, self.select_first_directory)
        create_button(self, review, xb, yb2, self.select_second_directory)
        self.button_review = create_button(self, review, xb, yb2 + 60, self.select_third_directory)
        self.button_review.hide()
        self.button_run = create_button(self, run, xb, yb3, self.check_radio_buttons)


    
    # Проверка задания двух путей
    def check_paths(self):
        if not self.first_path:
            fail(self, ErrorFromValue); return False
        elif not self.second_path:
            fail(self, ErrorToValue); return False
        elif not self.third_path and self.radio_dat.isChecked():
            fail(self, 'Введите третий путь'); return False
        return True



    def print_log(self,text):
        self.log_txt = text
        self.log_update.emit(1)


    def collect_files(self): 
        '''Many to one'''
        filename_list = []
        self.print_log(Begin_copy)
        for root, _, files in os.walk(self.first_path):
            for file in files:
                if file.endswith(txt):
                    to_path = f'{self.second_path}\\{splitName(root)[-1]}_{file}'
                    self.print_log(f"{root}\\{file} -> {to_path}")
                    shutil.copyfile(root + "\\" + file, to_path)
                    filename_list.append(to_path)
        
        self.print_log(End_copy)

        if self.checkbox.isChecked():
            xslx = f'{self.second_path}\Res'
            txt_to_xslx(filename_list,xslx)
            self.print_log(f'Files concatinate to file: {xslx}.xslx')
        return txt
  

    def send_out_file(self): 
        '''One to Many'''
        _exe = splitName(self.second_path, '/')[-1]
        _json = splitName(self.third_path, '/')[-1]
        for root, folders, _ in os.walk(self.first_path):
            for folder in folders:
                try:
                    shutil.copyfile(self.second_path, f'{root}\\{folder}\\{_exe}')
                    shutil.copyfile(self.third_path, f'{root}\\{folder}\\{_json}')
                except Exception as ex:
                    print(ex)
        return exe
  
  
    def move_dat_files(self):
        files = []
        files_list = []
        for root, _, files in os.walk(self.first_path):  
            for file in files:
                if file.endswith(dat) and file not in [f[1] for f in files_list]:
                    files_list.append([root, file])

        Count_files = len(files_list)
        split_list = [Count_files // split_count]*split_count
        split_list[-1] += Count_files % split_count
        self.print_log(make_directories(self.first_path, self.second_path, self.third_path))
        split_files(files_list,split_list)
        return dat




  
    def select_first_directory(self):
        self.first_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.first_line_edit.setText(self.first_path)


    def select_third_directory(self):
        self.third_path = str(QFileDialog.getOpenFileName(self,'Open File', None, '*.json')[0])
        self.third_line_edit.setText(self.third_path)
        

    def select_second_directory(self):
        if self.radio_dat.isChecked() or self.radio_exe.isChecked():
            self.second_path = str(QFileDialog.getOpenFileName(self,'Open File', None, '*.exe')[0])
        else:
            self.second_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.second_line_edit.setText(self.second_path)
        
