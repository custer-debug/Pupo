
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

chk1 = "Delete exe-files"
File = os.getcwd()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Cleaning program'
        self.setWindowIcon(QIcon('icon.png'))

        self.left = 700
        self.top = 300        
        self.checkBox_1 = QCheckBox(chk1, self)
        self.checkBox_1.move(20, 80)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedSize(480,27)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(File)

        flo = QFormLayout()
        flo.addRow(self.lineEdit)
        self.setLayout(flo)


        self.width = 620
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button1 = QPushButton('Run', self)
        button1.move(500,450)
        button1.clicked.connect(self.on_click)

        button2 = QPushButton('Exit', self)
        button2.clicked.connect(self.exit)
        button2.move(30,450)

        button3 = QPushButton('Review', self)
        button3.clicked.connect(self.selectDirectory)
        button3.move(500,10)
        self.show()

    @pyqtSlot()
    def on_click(self):
        path = str()
        if self.checkBox_1.isChecked() == True and len(File) != 0:
            for root, _, files in os.walk(File):
                for file in files:
                    if file.endswith(".exe"):
                        path = os.path.join(root, file)
                        os.remove(path)
                        print(path)
            if len(path) == 0:
                print("Files exe is not found")
        
    

    def selectDirectory(self):
        File = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit.setText(File)
    



    def exit(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()