import os
from datetime import datetime
from PyQt5.QtGui import QTextCursor
import logging
import shutil
from DefaultVariable import *
from pyexcel import save_as
from csv import reader
from PyQt5.QtWidgets import QCheckBox, QLabel, QRadioButton, QMessageBox, QPushButton
from json import dump


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







def make_directories(cwd,exe,json):
    text = ""
    for i in range(split_count):
        dir = f"{cwd}\Part_{str(i+1)}"
        try:
            os.makedirs(dir)
        except FileExistsError:
            text += f"Папка: {dir} уже существует <br>"

        shutil.copy(exe,dir + "\\" + exe.split('/')[-1])
        shutil.copy(json,dir + "\\" + json.split('/')[-1])

    if len(text) == 0:
        text = "Папки успешно созданы"
        
    return text        





def split_files(files,num): 
    for i in range(split_count):
        for _ in range(num[i]):
            file = files[0]
            From =  f"{file[0]}\\{file[1]}"
            To  = f"{file[0]}\\Part_{i+1}\\{file[1]}"
            try:
                shutil.move(From,To)
                files.remove(files[0])
            except FileNotFoundError:
                return 




def success(self, success, text):
    return QMessageBox.critical(self,success, text)




def fail(self, fail, text):
    return QMessageBox.information(self,fail, text)




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

    return "byte"



# Check fill info
def check_data_to_json(btn):
        for i in btn:
            if i.checkedButton() == None:
                return True
        return False


# Write to file config info 
def dict_to_json(dictinary):
    with open('config.json', 'w') as outfile:
        dump(dictinary, outfile, indent = 4)



# Create elements

def create_button(self, name, x,y, function):
    tmp = QPushButton(name,self)
    tmp.move(x,y)
    tmp.setFixedSize(wb,hb)
    tmp.clicked.connect(function)
    return tmp

def create_check_box(self, name, y):
    checkbox = QCheckBox(name, self)
    checkbox.move(check_boxes_x, y)
    checkbox.setFixedSize(check_boxes_wight, check_boxes_height)
    return checkbox

def create_label_function(self, title, y):
    label = QLabel(title,self)
    label.setStyleSheet(front)
    label.move(lx,y)
    return label 


def radio_button_create(self, name, x, y):
    radio = QRadioButton(name,self)
    radio.setFixedSize(rsize_x,rsize_y)
    radio.move(x,y)
    return radio




#   Главная функция удаления исполняемых файлов
def delete_files(self, cwd, extension):
    print('delete_files')

    path = ""
    Fsize = 0
    for root, _, files in os.walk(cwd):
            for file in files:
                if file.endswith(extension):
                    path = os.path.join(root, file)
                    Fsize += os.stat(path).st_size 
                    os.remove(path)
                    Print(self,"Удалён: " + path)
    
    Print(self,f'Очищено: {str(round(Fsize,2))} {size_of_file(Fsize)}')

    return False if len(path) == 0 else True


#   Функция поиска dat-файлов
def find_first_file(endswith, files):
    for file in files:
        print(file)
        if file.endswith(endswith):
            return file


#   Главная функция переименования выходных файлов
def hangle_rename_txt_file(self, cwd, arg = None):
    print('hangle_rename_txt_file')
    # rename = ""
    _bool = True
    for root, _, files in os.walk(cwd):
        dat_file = find_first_file(dat, files)
        txt_file = find_first_file(txt, files)
        if dat_file != None and txt_file != None:
            rename = f'{splitName(root)[-1]}_{splitDate(dat_file)}{txt}'
            Print(self,f'{root}\{txt_file} -> {root}\{rename}')
            _bool = False
        elif txt_file != None:
            rename = f'{splitName(root)[-1]}{txt}'
            Print(self, f'{root}\{txt_file} -> {root}\{splitName(root)[-1]}{txt}')
            _bool = False
        # try: 
        print(txt_file)
        os.rename(os.path.join(root, txt_file), os.path.join(root, rename))
        # except Exception:
            # continue
    # Print(self,"Done")

    
    return _bool



#   Удаление пустых директорий
def del_empty_dirs(self, path, arg = None):
    print('del_empty_dirs')
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
