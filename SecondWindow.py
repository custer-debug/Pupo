from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from DefaultVariable import *
import os
import shutil
from Function import * 


class SecondWindowClass(QMainWindow):
    log_update = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.first_path = ""
        self.second_path   = ""
        self.log_txt = ''
        self.radio_bool = False
        self.setWindowTitle(copy_files)
        self.setWindowIcon(QIcon(Icon_copy))

        first_label = QLabel(label_from,self)
        first_label.setStyleSheet(front)
        first_label.move(lx,y1)

        second_label = QLabel(label_to,self)
        second_label.setStyleSheet(front)
        second_label.move(lx,y2)
        
        self.first_label = first_label
        self.second_label = second_label

        self.default_variable()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()


    def default_variable(self):
        self.setGeometry(ax,ay,aw,ah)
        self.radio_buttons_create_function()
        self.line_edit_create_function()
        self.default_buttons_create_function()
        self.checkbox_create_function()

 
    def checkbox_create_function(self):
        self.checkbox = QCheckBox("Txt to xslx",self)
        self.checkbox.move(25,160)
        self.checkbox.setFixedSize(100,20)


    def radio_button_checked_function(self):
        if not self.radio_dat.isChecked():
            self.radio_bool = False
            self.setWindowTitle(copy_files)
            self.first_label.setText(label_from)
            self.second_label.setText(label_to)
            self.checkbox.setDisabled(False)
        else:
            self.radio_bool = True
            self.setWindowTitle(name_split)
            self.first_label.setText(label_Path)
            self.second_label.setText(label_exe)
            self.checkbox.setDisabled(True)




    def radio_buttons_create_function(self):
        radio_txt = QRadioButton(txt,self)
        radio_txt.setFixedSize(rsize_x,rsize_y)
        radio_txt.move(xr1,yr)
        radio_txt.setChecked(True)

        radio_dat = QRadioButton(dat,self)
        radio_dat.setFixedSize(rsize_x,rsize_y)
        radio_dat.move(xr2,yr)
        self.radio_dat = radio_dat
        group = QButtonGroup(self)
        group.addButton(radio_txt)
        group.addButton(radio_dat)
        group.buttonClicked.connect(self.radio_button_checked_function)


    def line_edit_create_function(self):
        self.first_line_edit = QLineEdit(self)
        first_line_edit = self.first_line_edit
        first_line_edit.setFixedSize(wl,hl)
        first_line_edit.move(xledit,yledit_1)

        self.second_line_edit = QLineEdit(self)
        second_line_edit = self.second_line_edit
        second_line_edit.setFixedSize(wl,hl)
        second_line_edit.move(xledit,yledit_2)


    def default_buttons_create_function(self):
        btn_sel_first_dir = QPushButton(review,self)
        btn_sel_first_dir.move(xb,yb1)
        btn_sel_first_dir.setFixedSize(wb,hb)
        btn_sel_first_dir.clicked.connect(self.select_first_directory)

        btn_sel_second_dir = QPushButton(review,self)
        btn_sel_second_dir.move(xb,yb2)
        btn_sel_second_dir.setFixedSize(wb,hb)
        btn_sel_second_dir.clicked.connect(self.select_second_directory)


        button_run = QPushButton(run,self)
        button_run.move(xb,yb3)
        button_run.setFixedSize(wb,hb)

        button_run.clicked.connect(self.check_radio_buttons)





    # Проверка задания двух путей
    def check_paths(self):
        if len(self.first_path) == 0:
            QMessageBox.critical(self,MessageError, ErrorFromValue)
            return True
        elif len(self.second_path) == 0:
            QMessageBox.critical(self, MessageError, ErrorToValue)
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


        
  
    def select_first_directory(self):
        self.first_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.first_line_edit.setText(self.first_path)

    def select_second_directory(self):
        if self.radio_dat.isChecked():
            self.second_path = str(QFileDialog.getOpenFileName(self,'Open File', None, '*.exe')[0])
        else:
            self.second_path = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.second_line_edit.setText(self.second_path)
        


