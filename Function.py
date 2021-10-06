import os
from datetime import datetime
from PyQt5.QtGui import QTextCursor
import logging
import shutil
from DefaultVariable import *

Text = ""
logging.basicConfig(filename='Pupo.log',level = logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')




#   Функция записи событий в окне статуса
def Print(self,text):
        global Text
        logging.info(text)
        Text += f'<b> [{str(datetime.now().strftime("%H:%M:%S"))}] </b> {text} <br> ' 
        self.Text.setHtml(Text)
        self.Text.moveCursor(QTextCursor.End)
        
    


def splitName(str):
    return str.split('\\')


def splitDate(str):
    s = str.split('_')
    s.pop(0)
    a = s[-1].split('.')
    s.pop(-1)
    s.append(a[0])
    res = '_'.join(s)
    return res


def del_empty_dirs(self, path):
        flag = True
        for d in os.listdir(path):
            a = os.path.join(path, d)
            if os.path.isdir(a):
                del_empty_dirs(self, a)
                if not os.listdir(a):
                    os.rmdir(a)
                    Print(self,"Папка удалена: " + a)
                    flag = False
        return flag


def make_directories(cwd,exe):
    text = ""
    for i in range(split_count):
        dir = f"{cwd}\Part_{str(i+1)}"
        try:
            os.makedirs(dir)
        except FileExistsError:
            text += f"Папка: {dir} уже существует <br>"

        shutil.copy(exe,dir + "\\" + exe.split('/')[-1])

    if len(text) == 0:
        text = "Папки успешно созданы"
    return text        



def split_files(files,num): 
    size = len(files)
    for i in range(10):
        for _ in range(num[i]):
            file = files[0]
            From =  f"{file[0]}\\{file[1]}"
            To  = f"{file[0]}\\Part_{i+1}\\{file[1]}"
            shutil.move(From,To)
            files.remove(files[0])
            print(f"Success: {size - len(files)} of {size}")
