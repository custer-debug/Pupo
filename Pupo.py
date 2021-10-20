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
        pixmapi = getattr(QStyle, 'SP_DialogResetButton')
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.setWindowTitle(TITLE_MAIN_WINDOW)
        self.setGeometry(WINDOW_X, WINDOW_Y, WINDOW_WIDHT, WINDOW_HEIGHT)

        self.button_handle_function()
        self.handle_checkbox_function()
        self.handle_line_edit_function()
        self.show() # Функция отображения окна


    #   Функция инициализации полей
    def handle_line_edit_function(self):
        self.main_line_edit = create_line_edit(self, LINE_EDIT_XY, LINE_EDIT_XY, MAIN_LINE_EDIT_WIDHT)
        self.main_line_edit.setText(os.getcwd().replace('/', '\\'))

        self.line_extension = create_line_edit(self, LINE_EXTENSION_X, LINE_EXTENSION_Y, LINE_EXTENSION_WIDHT, LINE_EXTENSION_NAMEFILE_HIEGHT)
        self.line_extension.setDisabled(True)
        self.line_extension.setText(EXE)

        self.line_name_file = create_line_edit(self, LINE_NAMEFILE_X, LINE_NAMEFILE_Y, LINE_NAMEFILE_WIDHT, LINE_EXTENSION_NAMEFILE_HIEGHT)
        self.line_name_file.setDisabled(True)
        self.line_name_file.setText(OUT_RES)

        self.Text = QTextBrowser(self)
        self.Text.move(TEXT_FIELD_X,TEXT_FILED_Y)
        self.Text.setFixedSize(TEXT_FILED_WIDHT,TEXT_FILED_HEIGHT)


    def enabled_line_delete(self):
        return self.line_extension.setDisabled(False) if self.checkbox_delete.isChecked() else self.line_extension.setDisabled(True)

    def enabled_line_rename(self):
        return self.line_name_file.setDisabled(False) if self.checkbox_rename.isChecked() else self.line_name_file.setDisabled(True)



    def create_check_box(self, name, y):
        checkbox = QCheckBox(name, self)
        checkbox.move(CHECK_BOXES_X, y)
        checkbox.setFixedSize(CHECK_BOXES_WIGHT, CHECK_BOXES_HEIGHT)
        return checkbox

    #   Функция инициализации чекбоксов
    def handle_checkbox_function(self):

        self.checkbox_delete = self.create_check_box(MSG_DELETE_FILES, CHECK_BOX_Y1)
        self.checkbox_rename = self.create_check_box(MSG_RENAME_FILES, CHECK_BOX_Y2)
        self.checkbox_empty_dir = self.create_check_box(MSG_DELETE_EMPTY_DIR, CHECK_BOX_Y3)
        self.checkbox_delete.clicked.connect(self.enabled_line_delete)
        self.checkbox_rename.clicked.connect(self.enabled_line_rename)



    #   Функция инициализации кнопок
    def button_handle_function(self):
        create_button(self, TITLE_RUN, BUTTON_RUN_X, BUTTON_RUN_Y, self.on_click)
        create_button(self, TITLE_EXIT, BUTTON_EXIT_X, BUTTON_EXIT_Y, self.exit)
        create_button(self, TITLE_REVIEW, BUTTON_REVIEW_X, BUTTON_REVIEW_Y, self.select_main_directory)
        create_button(self, TITLE_MOVE, BUTTON_MOVE_X, BUTTON_MOVE_Y, self.open_copy_window)
        create_button(self, "Edit config file", X_BUTTON - 10,Y_BUTTON_3 - 15,self.open_window_edit_config)


    def open_window_edit_config(self):
        self.config = ConfigFile()
        self.config.show()

    def select_main_directory(self):
        File = str(QFileDialog.getExistingDirectory(self, select_dir)).replace('/', '\\')
        self.main_line_edit.setText(File)

    def open_copy_window(self):
        self.CopyWindow = CopyWindowClass()
        self.CopyWindow.log_update.connect(self.callback)
        self.CopyWindow.show()


    def callback(self):
        Print(self, self.CopyWindow.log_txt)
        QtGui.QGuiApplication.processEvents()




    def checked_some_box(self, check_box, text, function, extension = None):
        if check_box.isChecked() and function(self, self.main_line_edit.text(), extension):
            Print(self, text)
        check_box.setChecked(False)

    def check_boxes_default_view(self):
        self.checkbox_rename.setChecked(False)
        self.checkbox_delete.setChecked(False)
        self.checkbox_empty_dir.setChecked(False)
        self.enabled_line_rename()
        self.enabled_line_delete()


    @pyqtSlot()
    def on_click(self):
        self.checked_some_box(self.checkbox_delete, MSG_FILES_NOT_FOUND, delete_files,self.line_extension.text())
        self.checked_some_box(self.checkbox_rename, MSG_FILES_NOT_FOUND, handle_rename_txt_file, self.line_name_file.text())
        self.checked_some_box(self.checkbox_empty_dir, MSG_EMPTY_DIR_NOT_FOUND, del_empty_dirs)
        self.check_boxes_default_view()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()
