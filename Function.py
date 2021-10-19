import os
from datetime import datetime
from PyQt5.QtGui import QTextCursor
import logging
import shutil
from DefaultVariable import *
from pyexcel import save_as
from csv import reader
from PyQt5.QtWidgets import *
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
        


def splitName(str, sep = '\\'):
    return str.split(sep)




def splitDate(str):
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



def fail(self, text):
    return QMessageBox.critical(self,MsgSuccess, text)


def success(self, text):
    return QMessageBox.information(self,MessageError, text)




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

def create_line_edit(self, x, y, w, h = line_edit_height):
    line_edit = QLineEdit(self)
    line_edit.setFixedSize(w,h)
    line_edit.move(x,y)
    return line_edit


#   Главная функция удаления исполняемых файлов
def delete_files(self, cwd, extension):
    # print(f'{extension}')
    path = ''
    Fsize = 0
    res = True
    count = 0
    # print(cwd)
    if not extension: return res

    for root, _, files in os.walk(cwd):
            for file in files:
                if file.endswith(extension):
                    print(root+'\\'+file)
                    path = os.path.join(root, file)
                    Fsize += os.stat(path).st_size 
                    os.remove(path)
                    Print(self,"Удалён: " + path)
                    res = False
                    count += 1
    i = 0 
    while Fsize > 1000:
        Fsize /= 1024  
        i += 1
    Print(self,f'Очищено:{count} файлов. Общий размер: {round(Fsize,2)} {Size[i]}.')

    return res


def find_first_file(enswitch, files):
    for file in files:
        if file.endswith(enswitch):
            return file
    return None


def generate_filename_with_dat_file(root,dat_file):
    return f'{splitName(root)[-1]}_{splitDate(dat_file)}{txt}'

def generate_filename_without_dat_file(root):
    return f'{splitName(root)[-1]}{txt}'


#   Главная функция переименования выходных файлов
def handle_rename_txt_file(self, cwd, arg = None):
    rename = ''
    _bool = True
    for root, _, files in os.walk(cwd):

        dat_file = find_first_file(dat, files)
        txt_file = find_first_file(out_res, files)
        print(txt_file)
        if dat_file == None and txt_file == None:
            continue
         
        if dat_file != None and txt_file != None:
            rename = generate_filename_with_dat_file(root,dat_file)
            Print(self,f'{root}\{txt_file} -> {root}\{rename}')
            _bool = False
        elif txt_file != None:
            rename = generate_filename_without_dat_file(root)
            Print(self, f'{root}\{txt_file} -> {root}\{splitName(root)[-1]}{txt}')
            _bool = False
        try:
            os.rename(os.path.join(root, txt_file), os.path.join(root, rename))
        except Exception as ex:
            print(ex)
            continue         
                
    return _bool



#   Удаление пустых директорий
def del_empty_dirs(self, path, arg = None):
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
