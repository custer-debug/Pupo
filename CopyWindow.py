import re
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
        self.setWindowTitle(copy_files)
        self.setWindowIcon(QIcon(Icon_copy))
        


        self.default_variable()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()


    def default_variable(self):
        self.setGeometry(ax,ay,aw,ah)
        self.label_handle()
        self.radio_button_handle()
        self.line_edit_handle()
        self.button_handle()
        self.checkbox_create_function()

 
    def checkbox_create_function(self):
        self.checkbox = QCheckBox("Txt to xslx",self)
        self.checkbox.move(25,160)
        self.checkbox.setFixedSize(100,20)

    def change_elements_option_function(self,bool,title, first_label, second_label,height, btn_y,checkbox_bool):
        self.radio_bool = bool
        self.setWindowTitle(title)
        self.first_label.setText(first_label)
        self.second_label.setText(second_label)
        self.checkbox.setDisabled(bool)
        self.setGeometry(ax,ay,aw,height)
        self.button_run.move(xb,btn_y)
        self.button_config.move(xb - 100, btn_y)
        if checkbox_bool:
            self.checkbox.hide()
            self.third_line_edit.show()
            self.third_label.show()
            self.button_config.show()
            self.button_review.show()
        else: 
            self.button_config.hide()
            self.button_review.hide()
            self.checkbox.show()
            self.third_line_edit.hide()
            self.third_label.hide()

        

    def create_label_function(self, title, y):
        label = QLabel(title,self)
        label.setStyleSheet(front)
        label.move(lx,y)
        return label 

    def label_handle(self):
        self.first_label = self.create_label_function(label_from, y1)
        self.second_label = self.create_label_function(label_to, y2)
        self.third_label = self.create_label_function("Json: ", y2 + 60)
        self.third_label.hide()

    def radio_button_checked_function(self):
        if not self.radio_dat.isChecked():
            self.change_elements_option_function(False, copy_files, label_from, label_to,ah,yb3, False)
        else:
            self.change_elements_option_function(True, name_split, label_Path, label_exe,260,yb3 + 60, True)

    def radio_button_create(self, name, x):
        radio = QRadioButton(name,self)
        radio.setFixedSize(rsize_x,rsize_y)
        radio.move(x,yr)
        return radio

    def radio_button_handle(self):
        radio_txt = self.radio_button_create(txt,xr1)
        radio_txt.setChecked(True)
        radio_dat = self.radio_button_create(dat,xr2)
        self.radio_dat = radio_dat

        group = QButtonGroup(self)
        group.addButton(radio_txt)
        group.addButton(radio_dat)
        group.buttonClicked.connect(self.radio_button_checked_function)


    def line_edit_create(self, y):
        line_edit = QLineEdit(self)
        line_edit.setFixedSize(wl,hl)
        line_edit.move(xledit,y)
        return line_edit

    def line_edit_handle(self):
        self.first_line_edit = self.line_edit_create(yledit_1)
        self.second_line_edit = self.line_edit_create(yledit_2)
        self.third_line_edit = self.line_edit_create(yledit_2 + 60)
        self.third_line_edit.hide()
        

    def button_create(self, name, x,y, function):
        tmp = QPushButton(name,self)
        tmp.move(x,y)
        tmp.setFixedSize(wb,hb)
        tmp.clicked.connect(function)
        return tmp
        

    def button_handle(self):
        self.button_create(review, xb, yb1, self.select_first_directory)
        self.button_create(review, xb, yb2, self.select_second_directory)
        self.button_review = self.button_create(review, xb, yb2 + 60, self.select_third_directory)
        self.button_review.hide()
        self.button_run = self.button_create(run, xb, yb3, self.check_radio_buttons)
        self.button_config = self.button_create("Edit config file", xb - 100, yb3, self.open_window_edit_config)

    def open_window_edit_config(self):
        pass
    # Проверка задания двух путей
    def check_paths(self):
        if self.first_path == '':
            QMessageBox.critical(self,MessageError, ErrorFromValue)
            return True
        elif self.second_path == '':
            QMessageBox.critical(self, MessageError, ErrorToValue)
            return True
        elif self.third_path == '':
            QMessageBox.critical(self, MessageError, 'Введите третий путь')
            return True

        return False



    def print_log(self,text):
        self.log_txt = text
        self.log_update.emit(1)

    def copy_txt_files(self):
        filename_list= []
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
        self.print_log(make_directories(self.first_path, self.second_path))
        split_files(files_list,split_list)





    def check_radio_buttons(self):
        if self.check_paths():
            return
        
        if self.radio_bool:
            self.move_dat_files()
            QMessageBox.information(self, MsgSuccess, SplitSucces)
        else:
            self.copy_txt_files()
            QMessageBox.information(self, MsgSuccess, SuccessCopyFiles)


    def select_third_directory(self):
        self.third_path = str(QFileDialog.getOpenFileName(self,'Open File', None, '*.json')[0])
        self.third_line_edit.setText(self.third_path)
        
  
    def select_first_directory(self):
        self.first_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.first_line_edit.setText(self.first_path)

    def select_second_directory(self):
        if self.radio_dat.isChecked():
            self.second_path = str(QFileDialog.getOpenFileName(self,'Open File', None, '*.exe')[0])
        else:
            self.second_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.second_line_edit.setText(self.second_path)
        


