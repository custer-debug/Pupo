from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QListWidgetItem
import os
from xlsxwriter.workbook import Workbook
from xlsxwriter.exceptions import DuplicateWorksheetName
import csv
from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, BodyLabel
from PySide6.QtCore import QUrl


class SheetNameDialog(MessageBoxBase):
    def __init__(self, sheet_name: str, mode: int = 0, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = SubtitleLabel("Ошибка", self)
        self.count_symbols_label = BodyLabel(f"{len(sheet_name)}")
        self.sheet_name_le = LineEdit(self)
        self.sheet_name_le.setPlaceholderText("Имя листа")
        self.sheet_name_le.setClearButtonEnabled(True)
        self.sheet_name_le.setText(sheet_name)
        match mode:
            case 0:
                self.info_label = BodyLabel(
                    f"При склейки файла '{sheet_name}' произошла ошибка.\nНазвание листа в эксель не может быть больше 32 символов.\nВведите другое название или пропустите этот файл!"
                )
            case 1:
                self.info_label = BodyLabel(
                    f"Лист с именем '{sheet_name}' уже существует в файле. Введите уникальное имя для листа!"
                )
        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.info_label)
        self.viewLayout.addWidget(self.count_symbols_label)
        self.viewLayout.addWidget(self.sheet_name_le)
        # change the text of button
        self.yesButton.setText("Сохранить")
        self.cancelButton.setText("Пропустить")

        self.widget.setMinimumWidth(350)
        self.yesButton.setDisabled(True)
        self.sheet_name_le.textChanged.connect(self._validateUrl)

    def _validateUrl(self, text):
        self.count_symbols_label.setText(str(len(text)))
        self.yesButton.setEnabled(QUrl(text).isValid() and len(text) < 32)

    def get_name(self) -> str:
        return self.sheet_name_le.text()


class ExistsFile(MessageBoxBase):
    def __init__(self, filename: str, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = SubtitleLabel("Внимание", self)
        self.info_label = BodyLabel(
            f"Файл с именем: '{filename}' уже существует. Перезапиписать?"
        )
        self.yesButton.setText("Выполнить")
        self.cancelButton.setText("Отменить")

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.info_label)


class Converter:
    def __init__(self, main) -> None:
        self.main = main
        self.files = []
        self.selected_items = []
        self.main.convert_review_btn.clicked.connect(
            lambda: self.review_btn_handler(self.main.convert_findpath_le)
        )
        self.main.convert_find_btn.clicked.connect(self.find_btn_handler)
        self.main.convert_listwidget.itemClicked.connect(self.list_handler)
        self.main.convert_pathsave_review_btn.clicked.connect(
            lambda: self.review_btn_handler(self.main.convert_pathsave_le)
        )
        self.main.convert_run_btn.clicked.connect(self.run_btn_handler)
        self.main.convert_pathsave_le.setText(os.getcwd())
        self.main.convert_findpath_le.setText(os.getcwd())
        self.initial_mode_tbtn()

    def initial_mode_tbtn(self):
        self.main.buttonGroup_2.setId(self.main.many_to_one_tbtn, 0)
        self.main.buttonGroup_2.setId(self.main.many_to_many_tbtn, 1)

    def review_btn_handler(self, line_edit):
        path = QFileDialog.getExistingDirectory(self.main, "Select directory")
        if not path:
            return
        line_edit.setText(path)

    def find_btn_handler(self):
        path = self.main.convert_findpath_le.text()
        if not path:
            return self.main.error_msg("Выберите путь для поиска файлов!")

        if not os.path.exists(path):
            return self.main.error_msg("Такого пути не сущетсвует!")

        self.find_files(path)
        self.main.convert_listwidget.clear()
        self.main.convert_listwidget.addItems(self.files)

    def find_files(self, path):
        self.files.clear()
        for cwd, _, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    self.files.append(os.path.join(cwd, file))

    def list_handler(self, item: QListWidgetItem = None):
        self.selected_items = self.main.convert_listwidget.selectedItems()
        self.main.convert_count_selected_row_label.setText(
            str(len(self.selected_items))
        )

    def run_btn_handler(self):
        if not self.main.convert_pathsave_le.text():
            return self.main.error_msg("Выберите путь для сохранения!")

        if not self.selected_items:
            return self.main.error_msg("Выберите файлы для склейки!")

        name = os.path.join(
            self.main.convert_pathsave_le.text(),
            self.main.convert_name_savefile_le.text(),
        )
        name += ".xlsx"
        if os.path.exists(name):
            e = ExistsFile(name, self.main)
            if not e.exec():
                return self.main.error_msg("Операция прервана!")

        match self.main.buttonGroup_2.checkedId():
            case 0:
                self.many_to_one(name)
            case 1:
                self.many_to_many(name)

    def many_to_many(self, name: str):
        workbook = Workbook(name)
        for item in self.selected_items:
            file = item.text()
            tmp = os.path.basename(file)
            sheet_name = tmp
            if len(tmp) >= 32:
                new_sheet_name_dialog = SheetNameDialog(
                    sheet_name=tmp, parent=self.main
                )
                if new_sheet_name_dialog.exec():
                    sheet_name = new_sheet_name_dialog.get_name()
                else:
                    continue
            try:
                worksheet = workbook.add_worksheet(sheet_name)
            except DuplicateWorksheetName:
                new_sheet_name_dialog = SheetNameDialog(
                    sheet_name=tmp, mode=1, parent=self.main
                )
                if new_sheet_name_dialog.exec():
                    worksheet = workbook.add_worksheet(new_sheet_name_dialog.get_name())
                else:
                    continue

            with open(file, "rt", encoding="Windows-1251") as f:
                reader = csv.reader(f, delimiter="\t")
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        try:
                            col = float(col.replace(",", "."))
                        except ValueError:
                            ...
                        worksheet.write(r, c, col)
        workbook.close()
        return self.main.success_msg("Файлы успешно склеины!")

    def many_to_one(self, name: str):
        workbook = Workbook(name)
        worksheet = workbook.add_worksheet("Sheet")
        row_ = 0
        for item in self.selected_items:
            file = item.text()
            with open(file, "rt", encoding="Windows-1251") as f:
                reader = csv.reader(f, delimiter="\t",)
                if row_ != 0:
                    next(reader)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        try:
                            col = float(col.replace(",", "."))
                        except ValueError:
                            ...
                        worksheet.write(row_, c, col)
                    row_ += 1
        print(row_)
        workbook.close()
        return self.main.success_msg("Файлы успешно склеины!")
