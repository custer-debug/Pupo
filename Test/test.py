from PyQt5.QtWidgets import QMessageBox

QMessageBox.information(self, 'Справка',
open('Readme.md', 'r', encoding='utf-8').read())
