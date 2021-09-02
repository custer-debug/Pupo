import os
import shutil
from PyQt5.QtWidgets import *

cwd = os.getcwd()
print(cwd)
files = []
files_list = []
for root, dirs, files in os.walk(cwd):  
    for file in files:
        if file.endswith(".dat") and file not in [f[1] for f in files_list]:
            files_list.append([root, file])


files = [os.path.join(f[0], f[1]) for f in files_list]
folders = set()
for i in range(len(files)):
    file = files_list[i][1]
    folders.add(files_list[i][0])
    shutil.move(f"{files[i]}", f"{cwd}\\{file}")

for i in folders:
    if i != cwd:
        print(f"Удалена папка {i}")
        shutil.rmtree(i,ignore_errors=True)



class CopyDatFiles():

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Copy Files")
        label_1 = QLabel("From: ",self)
        label_1.setStyleSheet("font: bold 12px")
        label_1.move(10,15)

        label_2 = QLabel("To: ",self)
        label_2.setStyleSheet("font: bold 12px")
        label_2.move(10,70)

        ax = 400
        ay = 200        
        
        aw = 600
        ah = 180

        self.setGeometry(ax,ay,aw,ah)
        self.show()
    

