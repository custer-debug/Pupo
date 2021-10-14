from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from DefaultVariable import *
from Function import *

class ConfigFile(QMainWindow):
    def __init__(self):
        super().__init__()
        x = y = 500
        a = 300
        self.setWindowTitle("Config")
        self.setGeometry(x,y,a,a)
        self.button_handle()
        self.label_handle()
        self.radio_button_handle()
        self.show()


    def label_handle(self):
        for item in title_label_json:
            create_label_function(self, item, title_label_json[item])



    def create_group_button(self, firstname, secondname, y):
        group = QButtonGroup(self)
        group.addButton(radio_button_create(self, firstname, 90,y)) 
        group.addButton(radio_button_create(self, secondname, 150,y)) 
        return group 


    def radio_button_handle(self):
        self.btn = [
            self.create_group_button('1200', '2500', 10),
            self.create_group_button('Local', 'Reson', 35),
            self.create_group_button('2', '4', 60)]   
        

    def create_button_function(self, name,x, y, function):
        btn = QPushButton(name, self)
        btn.move(x,y)
        btn.clicked.connect(function)
        btn.setFixedSize(btn_wight,btn_height)


    def button_handle(self):
        self.create_button_function("Save", 190, 250, self.button_checked_function)
        
    def compile_dict(self):
        for label,text in zip(title_label_json,self.btn):
            label.replace(': ', '')
            try:
                temp = int(text.checkedButton().text())
            except ValueError:
                temp = text.checkedButton().text()

            res_dict[label] = temp
        

    def button_checked_function(self):
        for i in self.btn:
            if i.checkedButton() == None:
                QMessageBox.critical(self, MessageError, "Выберите все нужные параметры")
                return

        self.compile_dict()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConfigFile()
    app.exec_()


