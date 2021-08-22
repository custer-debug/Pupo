import os
from datetime import datetime
from PyQt5.QtGui import QTextCursor
from Function import *
import logging

Text = ""
logging.basicConfig(filename='Pupo.log',level = logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')




#   Функция записи событий в окне статуса
def Print(self,text):
        global Text
        logging.info(text)
        Text += "<b>[" + str(datetime.now().strftime("%H:%M:%S")) + "]</b> " + text + "<br> " 
        self.Text.setHtml(Text)
        self.Text.moveCursor(QTextCursor.End)
        
        




def splitName(str):
    return str.split('\\')[-1]


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
        #Print(self,"Done")
        return flag

