import os
from datetime import datetime
from PyQt5.QtGui import QTextCursor
import logging
import shutil
from DefaultVariable import *
from pyexcel import save_as
from csv import reader

Text = ""
logging.basicConfig(filename='Pupo.log',level = logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')




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
    # print(str)
    s = str.split('_')
    s.pop(0)
    try:
        a = s[-1].split('.')
        s.pop(-1)
        s.append(a[0])
    except IndexError:
        return None
    res = '_'.join(s)
    return res




def del_empty_dirs(self, path):
        flag = False
        for d in os.listdir(path):
            a = os.path.join(path, d)
            if os.path.isdir(a):
                del_empty_dirs(self, a)
                if not os.listdir(a):
                    os.rmdir(a)
                    Print(self,"Папка удалена: " + a)
                    flag = True
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
    for i in range(10):
        for _ in range(num[i]):
            file = files[0]
            From =  f"{file[0]}\\{file[1]}"
            To  = f"{file[0]}\\Part_{i+1}\\{file[1]}"
            shutil.move(From,To)
            files.remove(files[0])






def txt_to_xslx(csv_list, path):
    
    all = [first_row]
    for f in csv_list:
        with open(f,'r') as fin:
            cr = reader(fin, delimiter='\t')
            filecontents = [line for line in cr]


        for line in filecontents:
            for x in range(1, len(line)-1):
                line[x] = line[x].replace(' ', '')
                line[x] = float(line[x])
                try:
                    line[x] = line[x].replace('.dat', '').replace('.', ',')
                except AttributeError:
                    continue
            line.pop(-1)

        all.extend(filecontents)
    save_as(array=all, start_row=0, sheet_name='List 1', dest_file_name = path + '.xlsx')


def size_of_file(file_size):

    if file_size >= 1024: #byte -> kilobyte
        file_size /= 1024
        return "Kb"

    if file_size >= 1024: #kilobyte -> megabyte
        file_size /= 1024
        return "Mb"

    if file_size >= 1024: #megabyte -> gigabyte 
        file_size /= 1024
        return "Gb" 



