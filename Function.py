import os
from datetime import datetime
from PyQt5.QtGui import QTextCursor

Text = ""

#   Функция записи событий в окне статуса
def Print(self,text):
        global Text
        Text += "[" + str(datetime.now().strftime("%H:%M:%S")) + "] " + text + "\n"
        self.Text.setText(Text)
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


def del_empty_dirs(path):
        flag = False
        for d in os.listdir(path):
            a = os.path.join(path, d)
            if os.path.isdir(a):
                del_empty_dirs(a)
                if not os.listdir(a):
                    os.rmdir(a)
                    print(a, 'удалена')
                    flag = True
        return flag