from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from DefaultVariable import *
import os
import shutil





def splitName(str):
    return str.split('\\')


class CopyWindow(QMainWindow):
    log_update = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.From = ""
        self.To   = ""
        self.Exe  = ""
        self.log_txt = ''
        self.radio_bool = False
        self.setWindowTitle(copy_files)
        # self.setWindowIcon(QIcon('Icon_copy.png'))

        label_From = QLabel(label_from,self)
        label_From.setStyleSheet(front)
        label_From.move(lx,y1)

        label_To = QLabel(label_to,self)
        label_To.setStyleSheet(front)
        label_To.move(lx,y2)

        label_Exe = QLabel(label_exe, self)
        label_Exe.setStyleSheet(front)
        label_Exe.move(lx,y3)

        
        self.default_variable()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()


    def default_variable(self):
        self.setGeometry(ax,ay,aw,ah)
        self.radio_buttons_variable()
        self.line_edit_variable()
        self.default_buttons_variable()

 


    def radio_button_checked_function(self,button):
        if button.text() == txt:
            self.radio_bool = False
            self.third_line_edit.setDisabled(True)
            self.setWindowTitle(copy_files)
            self.button_select_exe.setDisabled(True)
        else:
            self.radio_bool = True
            self.third_line_edit.setDisabled(False)
            self.setWindowTitle(name_split)
            self.button_select_exe.setDisabled(False)




    def radio_buttons_variable(self):
        radio_txt = QRadioButton(txt,self)
        radio_txt.setFixedSize(rsize_x,rsize_y)
        radio_txt.move(xr1,yr)
        radio_txt.setChecked(True)

        radio_dat = QRadioButton(dat,self)
        radio_dat.setFixedSize(rsize_x,rsize_y)
        radio_dat.move(xr2,yr)

        group = QButtonGroup(self)
        group.addButton(radio_txt)
        group.addButton(radio_dat)
        group.buttonClicked.connect(self.radio_button_checked_function)


    def line_edit_variable(self):
        self.first_line_edit = QLineEdit(self)
        first_line_edit = self.first_line_edit
        first_line_edit.setFixedSize(wl,hl)
        first_line_edit.move(xledit,yledit_1)

        self.second_line_edit = QLineEdit(self)
        second_line_edit = self.second_line_edit
        second_line_edit.setFixedSize(wl,hl)
        second_line_edit.move(xledit,yledit_2)

        self.third_line_edit = QLineEdit(self)
        third_line_edit = self.third_line_edit

        third_line_edit.setFixedSize(wl,hl)
        third_line_edit.move(xledit,yledit_3)
        third_line_edit.setDisabled(True)


    def default_buttons_variable(self):
        btn_sel_first_dir = QPushButton(review,self)
        btn_sel_first_dir.move(xb,yb1)
        btn_sel_first_dir.setFixedSize(wb,hb)
        btn_sel_first_dir.clicked.connect(self.select_first_directory)

        btn_sel_second_dir = QPushButton(review,self)
        btn_sel_second_dir.move(xb,yb2)
        btn_sel_second_dir.setFixedSize(wb,hb)
        btn_sel_second_dir.clicked.connect(self.select_second_directory)

        button_select_exe = QPushButton(review,self)
        self.button_select_exe = button_select_exe
        button_select_exe.move(xb,yb3)
        button_select_exe.setFixedSize(wb,hb)
        button_select_exe.clicked.connect(self.select_third_directory)
        button_select_exe.setDisabled(True)

        button_run = QPushButton(run,self)
        button_run.move(xb,yb4)
        button_run.setFixedSize(wb,hb)

        button_run.clicked.connect(self.check_radio_buttons)


    # Проверка задания двух путей
    def check_paths(self):
        if len(self.From) == 0:
            QMessageBox.critical(self,MessageError, ErrorFromValue)
            return True
        elif len(self.To) == 0:
            QMessageBox.critical(self, MessageError, ErrorToValue)
            return True
        return False



    def print_log(self,text):
        self.log_txt = text
        self.log_update.emit(1)

    def copy_txt_files(self):
        self.print_log(Begin_copy)
        for root, _, files in os.walk(self.From):
            for file in files:
                if file.endswith(txt):
                    self.print_log(f"{root}\\{file} -> {self.To}\\{splitName(root)[-1]}{txt}")
                    # shutil.copyfile(root + "\\" + file, self.To + "\\" + splitName(root)[-2] + "_" + splitName(root)[-1] + ".txt")
        self.print_log(End_copy)
        # self.log_update.emit(1)

  
  
  
  
    # def move_dat_files(self):
    #     files = []
    #     files_list = []
    #     for root, _, files in os.walk(self.From):  
    #         for file in files:
    #             if file.endswith(".dat") and file not in [f[1] for f in files_list]:
    #                 files_list.append([root, file])


    #     Count_files = len(files_list)
    #     split_num = []
    #     for i in range(10):
    #         split_num.append(Count_files // 10)
    #     split_num[-1] += Count_files % 10




    def check_radio_buttons(self):

        if self.check_paths():
            return
        
        if self.radio_bool:
            print("Hello world")
        else:
            self.copy_txt_files()
            QMessageBox.information(self, MsgSuccess, SuccessCopyFiles)
        

        # self.close()

        
  
    def select_first_directory(self):
        self.From = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.first_line_edit.setText(self.From)

    def select_second_directory(self):
        self.To = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.second_line_edit.setText(self.To)

    def select_third_directory(self):
        self.Exe = str(QFileDialog.getOpenFileName(self, "Open File",None, "*.exe")).replace('/', '\\')
        if self.Exe == "('', '')":
            self.third_line_edit.setText('')
        else:
            self.third_line_edit.setText(self.Exe)

