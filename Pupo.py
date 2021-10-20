import sys
import os
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui

# модули созданные специально для Pupo
from CopyWindow import CopyWindowClass
from ConfigFileHandle import ConfigFile
import Utilities as utils
import DefaultVariable as dv


class MainWindow(widgets.QMainWindow):

    def __init__(self):
        super().__init__()
        pixmapi = getattr(widgets.QStyle, 'SP_DialogResetButton')
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)
        self.setWindowTitle(dv.TITLE_MAIN_WINDOW)
        self.setGeometry(
            dv.WINDOW_X,
            dv.WINDOW_Y,
            dv.WINDOW_WIDHT,
            dv.WINDOW_HEIGHT)

        self.button_handle_function()
        self.handle_checkbox_function()
        self.handle_line_edit_function()
        self.show() # Функция отображения окна


    #   Функция инициализации полей
    def handle_line_edit_function(self):
        self.main_line_edit = utils.create_line_edit(self,
        dv.LINE_EDIT_XY,
        dv.LINE_EDIT_XY,
        dv.MAIN_LINE_EDIT_WIDHT)
        self.main_line_edit.setText(os.getcwd().replace('/', '\\'))

        self.line_extension = utils.create_line_edit(self,
            dv.LINE_EXTENSION_X,
            dv.LINE_EXTENSION_Y,
            dv.LINE_EXTENSION_WIDHT,
            dv.LINE_EXTENSION_NAMEFILE_HIEGHT)
        self.line_extension.setDisabled(True)
        self.line_extension.setText(dv.EXE)

        self.line_name_file = utils.create_line_edit(self,
            dv.LINE_NAMEFILE_X,
            dv.LINE_NAMEFILE_Y,
            dv.LINE_NAMEFILE_WIDHT,
            dv.LINE_EXTENSION_NAMEFILE_HIEGHT)
        self.line_name_file.setDisabled(True)
        self.line_name_file.setText(dv.OUT_RES)

        self.Text = widgets.QTextBrowser(self)
        self.Text.move(dv.TEXT_FIELD_X,dv.TEXT_FILED_Y)
        self.Text.setFixedSize(dv.TEXT_FILED_WIDHT,dv.TEXT_FILED_HEIGHT)


    def enabled_line_delete(self):
        return (
            self.line_extension.setDisabled(False)
            if self.checkbox_delete.isChecked()
            else self.line_extension.setDisabled(True))

    def enabled_line_rename(self):
        return (
            self.line_name_file.setDisabled(False)
            if self.checkbox_rename.isChecked()
            else self.line_name_file.setDisabled(True))



    # def create_check_box(self, name, y):
    #     checkbox = widgets.QCheckBox(name, self)
    #     checkbox.move(dv.CHECK_BOXES_X, y)
    #     checkbox.setFixedSize(dv.CHECK_BOXES_WIGHT, dv.CHECK_BOXES_HEIGHT)
    #     return checkbox

    def handle_checkbox_function(self):
        self.checkbox_delete = utils.create_check_box(dv.MSG_DELETE_FILES, dv.CHECK_BOX_Y1)
        self.checkbox_rename = utils.create_check_box(dv.MSG_RENAME_FILES, dv.CHECK_BOX_Y2)
        self.checkbox_empty_dir = utils.create_check_box(dv.MSG_DELETE_EMPTY_DIR, dv.CHECK_BOX_Y3)
        self.checkbox_delete.clicked.connect(self.enabled_line_delete)
        self.checkbox_rename.clicked.connect(self.enabled_line_rename)



    #   Обработчик кнопок
    def button_handle_function(self):
        utils.create_button(self,
        dv.TITLE_RUN,
        dv.BUTTON_RUN_X,
        dv.BUTTON_RUN_Y,
        self.on_click)

        utils.create_button(self,
        dv.TITLE_EXIT,
        dv.BUTTON_EXIT_X,
        dv.BUTTON_EXIT_Y,
        self.exit)

        utils.create_button(self,
        dv.TITLE_REVIEW,
        dv.BUTTON_REVIEW_X,
        dv.BUTTON_REVIEW_Y,
        self.select_main_directory)

        utils.create_button(self,
        dv.TITLE_MOVE,
        dv.BUTTON_MOVE_X,
        dv.BUTTON_MOVE_Y,
        self.open_copy_window)

        utils.create_button(self,
        dv.TITLE_CONFIG,
        dv.X_BUTTON - 10,
        dv.Y_BUTTON_3 - 15,
        self.open_window_edit_config)



    def open_window_edit_config(self):
        self.config = ConfigFile()
        self.config.show()

    def select_main_directory(self):
        path = str(widgets.getExistingDirectory(
            self,
            dv.SELECT_DIRECTORY)).replace('/', '\\')
        self.main_line_edit.setText(path)

    def open_copy_window(self):
        self.CopyWindow = CopyWindowClass()
        self.CopyWindow.log_update.connect(self.callback)
        self.CopyWindow.show()


    def callback(self):
        utils.Print(self, self.CopyWindow.log_txt)
        gui.QGuiApplication.processEvents()




    def checked_some_box(self, check_box, text, function, extension = None):
        if check_box.isChecked() and function(self, self.main_line_edit.text(), extension):
            utils.Print(self, text)
        check_box.setChecked(False)

    def check_boxes_default_view(self):
        self.checkbox_rename.setChecked(False)
        self.checkbox_delete.setChecked(False)
        self.checkbox_empty_dir.setChecked(False)
        self.enabled_line_rename()
        self.enabled_line_delete()


    def on_click(self):
        self.checked_some_box(
            self.checkbox_delete,
            dv.MSG_FILES_NOT_FOUND,
            utils.delete_files,
            self.line_extension.text())

        self.checked_some_box(
            self.checkbox_rename,
            dv.MSG_FILES_NOT_FOUND,
            utils.handle_rename_txt_file,
            self.line_name_file.text())

        self.checked_some_box(
            self.checkbox_empty_dir,
            dv.MSG_EMPTY_DIR_NOT_FOUND,
            utils.del_empty_dirs)

        self.check_boxes_default_view()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = widgets.QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()
