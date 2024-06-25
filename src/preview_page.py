from PySide6.QtWidgets import (
    QFileDialog,
    QHeaderView,
    QTableWidgetItem,
    QDialog,
    QVBoxLayout,
)
from src.templates.preview_settings import Ui_Dialog
from src.templates.graph import Ui_GraphUi
import csv
import pandas as pd
import numpy as np
import os
from PySide6.QtGui import QColor, QBrush
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class Settings(QDialog, Ui_Dialog):
    def __init__(self, columns, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.columns = columns
        self.save_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        self.preview_corr_cb.addItems(self.columns)
        self.preview_corr_cb_2.addItems(self.columns)
        self.preview_count_row_show_cb.addItems([str(2**i) for i in range(4, 11)])
        self.preview_corr_cb.currentTextChanged.connect(self.current_column_cb_handler)

    def current_column_cb_handler(self):
        self.preview_maxlimit_spin.setValue(0.0)
        self.preview_minlimit_spin.setValue(0.0)


class Graph(QDialog, Ui_GraphUi):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas,self)
        self._layout = QVBoxLayout(self.frame)
        self._layout.addWidget(self.toolbar,0)
        self._layout.addWidget(self.canvas,1)
        self._min_azimut = 0
        self._max_azimut = 360
        self._main_azimut = 0

    def exec_(self, distance:pd.Series, values:pd.Series):
        self.figure.clear()
        ax1 = self.figure.add_subplot(121,projection="polar")
        ax2 = self.figure.add_subplot(122)
        ax2.plot(distance,values,marker='o',linewidth=1,mfc='r')
        ax2.grid(True)
        ax1.set_theta_zero_location("N")
        ax1.set_theta_direction(-1)

        ax1.scatter(
            [np.deg2rad(self._main_azimut)] * distance.shape[0], distance, c="red", marker="."
        )
        ax1.set_thetamin(self._min_azimut)
        ax1.set_thetamax(self._max_azimut)
        self.canvas.draw()
        self.showMaximized()
        self.exec()

    @property
    def min_azimut(self): ...

    @min_azimut.setter
    def min_azimut(self, value: int):
        self._min_azimut = value

    @property
    def max_azimut(self): ...

    @max_azimut.setter
    def max_azimut(self, value: int):
        self._max_azimut = value

    @property
    def main_azimut(self): ...

    @main_azimut.setter
    def main_azimut(self, value: int):
        self._main_azimut = value


class PreviewFile:
    def __init__(self, main) -> None:
        self.main = main
        self.main.preview_review_btn.clicked.connect(self.select_file)
        self.path = os.getcwd()
        self.main.reset_link.clicked.connect(self.reset_colomn_color)

        self.main.min_link.clicked.connect(lambda: self.links_handler("min"))
        self.main.max_link.clicked.connect(lambda: self.links_handler("max"))
        self.main.set_params_link.clicked.connect(self.set_params_btn_handler)
        self.main.SwitchButton.checkedChanged.connect(self.switch_btn_handler)
        self.main.map_btn.clicked.connect(self.map_btn_handler)

        self.clear()
        self.hide_links()

    def select_file(self):
        self.file = QFileDialog.getOpenFileName(
            self.main, "Текстовый файл", self.path, "*.txt"
        )[0]
        if not self.file:
            return

        self.main.preview_current_file_label.setText(self.file)

        return self.read_file()

    def read_file(self):
        self.clear()

        with open(self.file) as r:
            reader = csv.reader(r, delimiter="\t")
            dataset = []
            cols = next(reader)
            cols[-1] = "Квадрупль"
            cols.append("")
            for line in reader:
                if len(line) > 18:
                    line = line[:18]
                dataset.append(line)
            self.df = pd.DataFrame(dataset, columns=cols)
        for col in self.df.columns:
            try:
                self.df[col] = (
                    self.df[col]
                    .apply(lambda x: str(x).replace(",", "."))
                    .astype("float")
                )
            except ValueError:
                continue
        self.columns = self.df.columns
        self.columns = [i for i in self.columns if i]
        dtypes = self.df.select_dtypes("float")
        self.df[dtypes.columns] = dtypes.abs()
        self.settings = Settings(self.columns, self.main)
        self.add_columns()
        self.fill_table()

        return self.main.success_msg(f"Открыт файл: {self.file}")

    def add_columns(self):
        self.main.preview_table.setColumnCount(len(self.columns))
        self.main.preview_table.setHorizontalHeaderLabels(self.columns)
        self.main.preview_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

    def fill_table(self):
        self.main.preview_table.setRowCount(self.rows_count)
        for row, line in zip(self.df.index, self.df.values):
            for col, value in enumerate(line):
                self.main.preview_table.setItem(row, col, QTableWidgetItem(str(value)))

    def links_handler(self, type_link: str):
        match type_link:
            case "min":
                row = self.df.loc[
                    (self.df.index < self.rows_count)
                    & (self.df[self.current_column] > 0.0),
                    self.current_column,
                ].idxmin()
            case "max":
                row = self.df.loc[
                    (self.df.index < self.rows_count)
                    & (self.df[self.current_column] > 0.0),
                    self.current_column,
                ].idxmax()
            case _:
                row = 0

        index = self.main.preview_table.model().index(row, self.current_column_num)
        self.main.preview_table.scrollTo(index)
        self.main.preview_table.selectRow(row)

    def set_links_text(self):
        if not self.current_column:
            return

        self.main.max_link.setText(str(self._max))
        self.main.min_link.setText(str(self._min))
        self.hide_links(False)

    def clear(self):
        self.df = None
        self.rows_count = 16
        self.current_column = ""
        self.current_column_num = 0
        self.settings = None
        self._max = 0
        self._min = 0
        self.hide_links()

    def reset_colomn_color(self):
        if not self.current_column:
            return
        self.paint_column(reset_state=True)

    def set_params_btn_handler(self):
        if self.settings is None:
            return self.main.error_msg("Выберите файл для предворительного просмотра!")

        if self.settings.exec():
            self.current_column = self.settings.preview_corr_cb.currentText()
            self.column_distance = self.settings.preview_corr_cb_2.currentText()
            self.rows_count = int(self.settings.preview_count_row_show_cb.currentText())
            change_rows_state = self.main.preview_table.rowCount() != self.rows_count

            tmp = self.settings.preview_minlimit_spin.value()
            self._min = tmp if tmp else self.get_min()

            tmp = self.settings.preview_maxlimit_spin.value()
            self._max = tmp if tmp else self.get_max()

            if change_rows_state:
                self.fill_table()

            if self.current_column != "Столбец":
                try:
                    self.current_column_num = self.df.columns.get_loc(
                        self.current_column
                    )
                    self.main.current_column_label.setText(self.current_column)
                    self.set_links_text()
                    self.paint_column()
                except Exception as e:
                    # print('Here')
                    return self.main.error_msg(str(e))



    def paint_column(self, reset_state: bool = False):
        _max = self._max
        # return
        seria_max = self.df.loc[
            self.df.index < self.rows_count, self.current_column
        ].div(_max)
        seria_max.replace([np.nan, -np.nan, np.inf, -np.inf], 0, inplace=True)
        if reset_state:
            seria_max.loc[:] = 0
        for row in range(self.main.preview_table.rowCount()):
            tmp = int(seria_max[row] * 255)
            color = tmp if tmp < 255 else 255
            self.main.preview_table.item(row, self.current_column_num).setForeground(
                QBrush(QColor(color, 0, 0))
            )

    def switch_btn_handler(self, state: bool):
        if "Квадрупль" not in self.df.columns:
            self.main.SwitchButton.setEnabled(False)
            return self.main.error_msg(
                "Столбца со значениями квадруполя нет в датасете!"
            )

        hidden_rows = self.df.loc[
            (self.df["Квадрупль"] == "") & (self.df.index < self.rows_count)
        ].index
        for row in hidden_rows:
            self.main.preview_table.setRowHidden(row, state)

    def hide_links(self, state: bool = True):
        if state:
            self.main.SwitchButton.hide()
            self.main.StrongBodyLabel_4.hide()
            self.main.StrongBodyLabel_5.hide()
            self.main.min_link.hide()
            self.main.max_link.hide()
        else:
            self.main.SwitchButton.show()
            self.main.StrongBodyLabel_4.show()
            self.main.StrongBodyLabel_5.show()
            self.main.min_link.show()
            self.main.max_link.show()

    def map_btn_handler(self):
        if not self.current_column:
            return

        distance = self.settings.distance_limit.value()
        limit_distance = distance if distance > 0 else 6000
        # print(self._min)
        res = self.df.loc[
            (self.df[self.current_column] < self._max)
            & (self.df[self.current_column] > self._min)
            & (self.df.index <= self.rows_count)
            & (self.df[self.column_distance] < limit_distance),
            :,
        ]
        res = res.loc[:,(self.column_distance,self.current_column)].sort_values(by=self.column_distance)
        x = res[self.column_distance]
        y = res[self.current_column]

        # print(res[[self.column_distance,self.current_column]].head(40))
        graph = Graph(self.main)
        min_a = self.settings.min_azimut.value()
        max_a = self.settings.max_azimut.value()
        graph.main_azimut = self.settings.main_azimut.value()
        if (min_a > max_a) or (max_a < min_a):
            min_a, max_a = max_a, min_a

        if m := min_a:
            graph.min_azimut = m
        if m := max_a:
            graph.max_azimut = m
        graph.exec_(x,y)

    def get_max(self) -> float:
        return self.df.loc[
            (self.df.index < self.rows_count) & (self.df[self.current_column] > 0.0),
            self.current_column,
        ].max()

    def get_min(self) -> float:
        return self.df.loc[
            (self.df.index < self.rows_count) & (self.df[self.current_column] > 0.0),
            self.current_column,
        ].min()
