from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox,QFileDialog
import sys
from platform import platform
import AdditionalFunction as af
import logging
from os import path

Form, _ = uic.loadUiType("Pupo.ui")
logging.basicConfig(level=logging.INFO, filename="pupo.log",filemode="a",
                    format="%(asctime)s %(lineno)d %(levelname)s %(message)s ")


class MainWindow(QtWidgets.QMainWindow, Form):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.main_menu_handler()
        self.del_files_tab_handler()
        self.move_files_tab_hanlder()
        self.concatenation_tab_hanlder()
        self.quitButton.clicked.connect(exit)



    def main_menu_handler(self):
        self.about_text.triggered.connect(self.msg_about)


    def msg_about(self):
        text = f'''
        Programm to Use Program Operations (Pupo)
        Version: 1.0.0
        Update: 2023-22-08
        OS: {platform()} 64-bit
        @Software engineers: \n\tKrekoten Roman Igorevich\n\tNenarokomov Maxim Dmitrievich
        '''
        return QMessageBox.information(self,'О программе', text)


    def del_files_tab_handler(self):
        self.reviewBtn.clicked.connect(
            lambda : self.del_line_edit.setText(
                QFileDialog.getExistingDirectory(None,"Select directory")))

        self.cb_del_files.toggled.connect(
            lambda: self.extension_line_edit.setEnabled(True) if self.cb_del_files.isChecked()
            else self.extension_line_edit.setEnabled(False))

        self.runBtn.clicked.connect(self.run_clean_up)


    def run_clean_up(self):
        if not self.del_line_edit.text():
            return QMessageBox.critical(self,'Ошибка','Не указан путь')

        try:
            if self.cb_del_files.isChecked():
                tmp = af.del_files(
                    self.del_line_edit.text(),
                    self.extension_line_edit.text())
                self.output_clean.setText(f'Выполнено. {tmp} удалено файлов')
                logging.info(f'{tmp} files removed')


            if self.cb_del_empty_dir.isChecked():
                tmp = af.delete_empty_directories(self.del_line_edit.text())
                self.output_clean.setText(f'Выполнено. {tmp} удалено папок')
                logging.info(f'{tmp} directories removed')

        except Exception as ex:
            logging.error(ex)
            print(ex)


    def move_files_tab_hanlder(self):
        self.reviewBtnFrom.clicked.connect(
            lambda : self.path_from_move.setText(
            QFileDialog.getExistingDirectory(None,"Select directory")))

        self.reviewBtnTo.clicked.connect(
            lambda : self.path_to_move.setText(
            QFileDialog.getExistingDirectory(None,"Select directory")))

        self.runBtn_2.clicked.connect(self.run_move_files)


    def run_move_files(self):
        if not self.path_from_move.text() or not self.path_to_move.text():
            return QMessageBox.critical(self,'Ошибка','Не указан путь')

        try:
            self.output_move_files.setText(
                af.copy_files(
                    self.path_from_move.text(),
                    self.path_to_move.text(),
                    self.cut_checkBox.isChecked()))
        except Exception as ex:
            print(ex)
            logging.error(ex)




    def concatenation_tab_hanlder(self):
        self.reviewBtn_concat.clicked.connect(
            lambda : self.concat_line_edit.setText(
            QFileDialog.getExistingDirectory(None,"Select directory")))


        self.reviewBtn_save_as.clicked.connect(
            lambda : self.save_as_line_edit.setText(
            QFileDialog.getExistingDirectory(None,"Select directory")))


        self.findBtn.clicked.connect(self.finder)
        self.select_all.clicked.connect(self.select_all_items)
        self.cancel_all.clicked.connect(self.cancel_all_items)
        self.run_concat.clicked.connect(self.run_concatenation)



    def finder(self):
        if not self.concat_line_edit.text():
            return QMessageBox.critical(self,'Ошибка','Не указан путь')
        self.list_results.clear()
        self.list_results.addItems(af.find_files(self.concat_line_edit.text()))
        self.list_results.itemClicked.connect(self.change_label_count)


    def change_state(self,flag):
        for item in range(self.list_results.count()):
            self.list_results.item(item).setSelected(flag)
        self.change_label_count()


    def select_all_items(self):
        return self.change_state(True)

    def cancel_all_items(self):
        return self.change_state(False)


    def change_label_count(self):
        return self.label_count.setText(str(len(self.list_results.selectedItems())))

    def run_concatenation(self):
        if not self.concat_line_edit.text() or not self.save_as_line_edit.text() or not self.filename_line_edit.text():
            return QMessageBox.critical(self,'Ошибка','Заполните все поля')

        if not self.list_results.selectedItems():
            return QMessageBox.critical(self,'Ошибка','Выберите элементы')

        save_file = path.join(
                    self.save_as_line_edit.text(),
                    self.filename_line_edit.text()+'.txt')

        if path.isfile(save_file):
            return QMessageBox.critical(self,'Ошибка', f'Файл {save_file} уже существует')

        try:
            tmp = af.concatenate(
                self.list_results.selectedItems(),
                save_file
                )
            return QMessageBox.about(self,'Готово',tmp)
        except Exception as ex:
            logging.error(ex)
            print(ex)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
