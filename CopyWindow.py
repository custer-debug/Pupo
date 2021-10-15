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
        print("Norm")

 
    def checkbox_handle_function(self):
        self.checkbox = create_check_box(self, "Txt to xslx", 160)



    def show_element(self):
        self.checkbox.hide()
        self.third_line_edit.show()
        self.third_label.show()
        self.button_review.show()

    def hide_element(self):
        self.button_review.hide()
        self.checkbox.show()
        self.third_line_edit.hide()
        self.third_label.hide()

    def change_elements_option_function(self,bool,title, first_label, second_label,height, btn_y,checkbox_bool):
        self.radio_bool = bool
        self.setWindowTitle(title)
        self.first_label.setText(first_label)
        self.second_label.setText(second_label)
        self.checkbox.setDisabled(bool)
        self.setGeometry(ax,ay,aw,height)
        self.button_run.move(xb,btn_y)
        if checkbox_bool:
            self.show_element()
        else: 
            self.hide_element()

        
    def label_handle(self):
        self.first_label = create_label_function(self,label_from, y1)
        self.second_label = create_label_function(self, label_to, y2)
        self.third_label = create_label_function(self, "Json: ", y2 + 60)
        self.third_label.hide()

    def radio_button_checked_function(self):
        if not self.radio_dat.isChecked():
            self.change_elements_option_function(False, copy_files, label_from, label_to,ah,yb3, False)
        else:
            self.change_elements_option_function(True, name_split, label_Path, label_exe,260,yb3 + 60, True)

    def radio_button_handle(self):
        radio_txt = radio_button_create(self, txt,xr1, yr)
        radio_txt.setChecked(True)
        radio_dat = radio_button_create(self, dat,xr2, yr)
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
        

    def button_handle(self):
        create_button(self, review, xb, yb1, self.select_first_directory)
        create_button(self, review, xb, yb2, self.select_second_directory)
        self.button_review = create_button(self, review, xb, yb2 + 60, self.select_third_directory)
        self.button_review.hide()
        self.button_run = create_button(self, run, xb, yb3, self.check_radio_buttons)


    
    # Проверка задания двух путей
    def check_paths(self):

        if self.first_path == '':
            success(self, MessageError, ErrorFromValue); return True

        elif self.second_path == '':
            success(self, MessageError, ErrorToValue); return True

        elif self.third_path == '' and self.radio_dat.isChecked():
            success(self, MessageError, 'Введите третий путь'); return True

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
        self.print_log(make_directories(self.first_path, self.second_path, self.third_path))
        split_files(files_list,split_list)





    def check_radio_buttons(self):
        if self.check_paths(): return
        
        if self.radio_bool:
            self.move_dat_files(); fail(self, MsgSuccess, SplitSucces) 
        else:
            self.copy_txt_files(); fail(self, MsgSuccess, SuccessCopyFiles) 

  
    def select_first_directory(self):
        self.first_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.first_line_edit.setText(self.first_path)


    def select_third_directory(self):
        self.third_path = str(QFileDialog.getOpenFileName(self,'Open File', None, '*.json')[0])
        self.third_line_edit.setText(self.third_path)
        

    def select_second_directory(self):
        if self.radio_dat.isChecked():
            self.second_path = str(QFileDialog.getOpenFileName(self,'Open File', None, '*.exe')[0])
        else:
            self.second_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.second_line_edit.setText(self.second_path)
        
