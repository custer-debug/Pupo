from PySide6.QtWidgets import QApplication, QMainWindow
from src.templates.ui_main_window import Ui_MainWindow
from src.collect_files_page import CollectFiles
from src.preview_page import PreviewFile
from src.convert_csv_to_xlsx import Converter
from qfluentwidgets import InfoBar

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_navigation_items()
        self.buttonGroup.idClicked.connect(
            lambda x: self.stackedWidget.setCurrentIndex(x)
        )
        self.collect_files = CollectFiles(self)
        self.preview_file = PreviewFile(self)
        self.converter = Converter(self)
        self.stackedWidget.setCurrentIndex(1)
        # self.connect_review_btns()
        # self.preview_count_row_show_cb.addItems(['10','20','50','100','150','200'])


    def init_navigation_items(self):
        self.buttonGroup.setId(self.collect_results_item, 0)
        self.buttonGroup.setId(self.preview_item, 1)
        self.buttonGroup.setId(self.convert_item, 2)




    def connect_review_btns(self):

        self.convert_review_btn.clicked.connect(
            lambda: self.select_directory(self.convert_findpath_le)
        )
        self.convert_pathsave_review_btn.clicked.connect(
            lambda: self.select_directory(self.convert_pathsave_le)
        )

    def error_msg(self, content:str):
        return InfoBar.error(
                title="Ошибка", content=content, duration=5000, parent=self
            )

    def success_msg(self, content:str):
        return InfoBar.success(
                title="Успех", content=content, duration=5000, parent=self
            )

if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec()
