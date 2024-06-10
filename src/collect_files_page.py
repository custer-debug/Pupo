import os
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt
import shutil
from datetime import date
import itertools


class CollectFiles:
    def __init__(self, main) -> None:
        self.main = main
        self.main.copy_run_btn.clicked.connect(self.copy_run_btn_handler)
        self.main.copy_from_path_btn.clicked.connect(
            lambda: self.select_directory(self.main.copy_from_path_le)
        )
        self.main.copy_to_path_btn.clicked.connect(
            lambda: self.select_directory(self.main.copy_to_path_le)
        )
        self.main.copy_prefix_cb.checkStateChanged.connect(
            lambda state: self.prefix_check_box_handler(state)
        )
        self.main.copy_postfix_cb.checkStateChanged.connect(
            lambda state: self.postfix_check_box_handler(state)
        )
        self.main.copy_prefix_datenow_cb.stateChanged.connect(self.prefix_cb_handler)
        self.main.copy_postfix_datenow_cb.stateChanged.connect(self.postfix_cb_handler)

    def prefix_cb_handler(self, state: int):
        state = bool(state)
        if state:
            self.main.copy_prefix_le.setText(date.strftime(date.today(), "%d_%m_%y"))
        else:
            self.main.copy_prefix_le.clear()

    def postfix_cb_handler(self, state: int):
        state = bool(state)
        if state:
            self.main.copy_postfix_le.setText(date.strftime(date.today(), "%d_%m_%y"))
        else:
            self.main.copy_postfix_le.clear()

    def is_paths_existing(self):
        """Проверка на существование путей во вкладке сбор результатов"""

        from_path = self.main.copy_from_path_le.text()
        to_path = self.main.copy_to_path_le.text()
        if not from_path:
            raise ValueError("Укажите директорию откуда копировать файлы")

        if not to_path:
            raise ValueError("Укажите директорию куда копировать файлы")

        if not os.path.exists(from_path):
            raise ValueError(f"Директории: {from_path} не существует")

        if not os.path.exists(to_path):
            raise ValueError(f"Директории: {to_path} не существует")

    def copy_run_btn_handler(self):
        try:
            self.is_paths_existing()
        except ValueError as e:
            return self.main.error_msg(str(e))

        files = self.find_files()
        if not files:
            return self.main.error_msg("Не найдено файлов для копирования")

        to = self.main.copy_to_path_le.text()

        if not to:
            return self.main.error_msg("Ошибка конечной директории")

        self.main.copy_output_te.clear()
        self.main.copy_progress_bar.setValue(0)

        size = len(files)

        for num, file in enumerate(files):
            basename = os.path.basename(file)
            dirname = os.path.split(os.path.dirname(file))[-1]
            name = dirname + "_" + basename

            if (
                self.main.copy_postfix_cb.isChecked()
                and self.main.copy_postfix_le.text()
            ):
                name, extension = name.split(".")
                name = f"{name}_{self.main.copy_postfix_le.text()}.{extension}"

            if self.main.copy_prefix_cb.isChecked() and self.main.copy_prefix_le.text():
                name = f"{self.main.copy_prefix_le.text()}_{name}"

            try:
                new_file = os.path.join(to, name)
                i = itertools.count()
                next(i)
                while os.path.exists(new_file):
                    name = name + f"({str(next(i))})"
                    new_file = os.path.join(os.path.join(to, name))

                shutil.copy(file, new_file)
            except Exception as e:
                print(e)
                return self.main.error_msg(f"Ошибка копирования файла {file}")

            self.main.copy_output_te.append(f"{file} --> {name}")
            self.main.copy_progress_bar.setValue(int((num + 1 / size)) * 100)

        if self.main.copy_cutmode_cb.isChecked():
            for file in files:
                try:
                    os.remove(file)
                    self.main.copy_output_te.append(f"Удален файл: {file}")
                except Exception:
                    return self.main.error_msg(f"Ошибка удаления файла {file}")

        self.main.copy_output_te.append(f"Скопировано: {size} файлов.")
        return self.main.success_msg(f"Файлы скопированы в папку: {to}")

    def find_files(self, extension: str = ".txt") -> list:
        result = []
        for cwd, _, files in os.walk(self.main.copy_from_path_le.text()):
            for file in files:
                if file.endswith(extension):
                    result.append(os.path.join(cwd, file))
        return result

    def select_directory(self, line_edit):
        path = QFileDialog.getExistingDirectory(self.main, "Select directory")
        if not path:
            return
        line_edit.setText(path)

    def prefix_check_box_handler(self, state):
        s = state == Qt.Checked
        if not s:
            self.main.copy_prefix_le.setText("")

        if not s:
            self.main.copy_prefix_datenow_cb.setChecked(False)

        self.main.copy_prefix_le.setEnabled(s)
        self.main.copy_prefix_datenow_cb.setEnabled(s)

    def postfix_check_box_handler(self, state):
        s = state == Qt.Checked
        if not s:
            self.main.copy_postfix_le.setText("")

        if not s:
            self.main.copy_postfix_datenow_cb.setChecked(False)

        self.main.copy_postfix_le.setEnabled(s)
        self.main.copy_postfix_datenow_cb.setEnabled(s)
