import logging
import sys
import os
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# модули созданные специально для Pupo
from CopyWindow import CopyWindowClass
from ConfigFileHandle import ConfigFile

from  Function import * 
from DefaultVariable import *


class MainWindow(QMainWindow):

# Функция инициализации окна
    def __init__(self):
        super().__init__()
        logging.info("\n <============>")
        pixmapi = getattr(QStyle, 'SP_DialogResetButton')
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.File =  os.getcwd().replace('/', '\\')
        
        self.setWindowTitle(Title)
        self.setGeometry(window_X, window_Y, window_Width, window_Height)

        self.button_handle_function()
        self.handle_checkbox_function()
        self.handle_line_edit_function()
        self.show() # Функция отображения окна


    #   Функция инициализации полей
    def handle_line_edit_function(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedSize(line_edit_wight,line_edit_height)
        self.lineEdit.setText(self.File)
        self.lineEdit.move(line_edit_xy,line_edit_xy)
        self.Text = QTextBrowser(self)
        self.Text.move(Text_X,Text_Y)
        self.Text.setFixedSize(Text_Wight,Text_Height)


    def create_check_box(self, name, y):
        checkbox = QCheckBox(name, self)
        checkbox.move(check_boxes_x, y)
        checkbox.setFixedSize(check_boxes_wight, check_boxes_height)
        return checkbox

    #   Функция инициализации чекбоксов
    def handle_checkbox_function(self):
        
        self.checkbox_delete = self.create_check_box(delete_exe_str, check_box1_y)
        self.checkbox_rename = self.create_check_box(rename_Out_res, check_box2_y)
        self.checkbox_empty_dir = self.create_check_box(delete_empty_dir, check_box3_y)

        
    #   Функция инициализации кнопок
    def button_handle_function(self):
        create_button(self, run, btn_run_x, btn_run_y, self.on_click)
        create_button(self, exit_, btn_exit_x, btn_exit_y, self.exit)
        create_button(self, review, btn_review_x, btn_review_y, self.select_main_directory)
        create_button(self, move_, btn_move_x, btn_move_y, self.open_copy_window)
        create_button(self, "Edit config file", xb - 10, yb3 - 5,self.open_window_edit_config)


    def open_window_edit_config(self):
        self.config = ConfigFile()
        self.config.show()

    def select_main_directory(self):
        self.File = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.lineEdit.setText(self.File)

    def open_copy_window(self):
        self.CopyWindow = CopyWindowClass()
        self.CopyWindow.log_update.connect(self.callback)
        self.CopyWindow.show()


    def callback(self):
        Print(self, self.w.log_txt)
        QtGui.QGuiApplication.processEvents()
        


    def checked_some_box(self, check_box, text, function, extension = None):
        if check_box.isChecked() and function(self, self.File, extension):
            Print(self, text)

    @pyqtSlot()
    def on_click(self):
        self.checked_some_box(self.checkbox_delete, exe_files_not_found, delete_files, exe)
        self.checked_some_box(self.checkbox_rename, Out_res_not_found, hangle_rename_txt_file)
        self.checked_some_box(self.checkbox_empty_dir, empty_dir_not_found, del_empty_dirs)
                       

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()








