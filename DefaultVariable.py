##############################
#-------> CopyWindow <-------#
##############################
from os import cpu_count
# количество частей разбиения dat-файлов
split_count = cpu_count()

Size = [
    'Byte',
    'Kilobyte',
    'Megabyte',
    'Gigabyte'
    'Terabyte'
]

# сообщения об успешном или ошибочном ты программы
ErrorFromValue = "Необходимо выбрать первый путь"
ErrorToValue   = "Необходимо выбрать второй путь"
ErrorExeValue = "Выберите exe-файл"
MessageError   = "Ошибка"
MsgSuccess = "Успех"
SuccessCopyFiles = "Файлы скопированы"
SplitSucces = "Файлы успешно разделены"
Begin_copy = "Начало копирования"
End_copy = "Конец копирования"

# название окна
name_split = 'Split dat-files'
copy_files = 'Copy txt-files'

# координаты расположения окна 
ax = 400
ay = 200        

# размер окна 
aw = 600
ah = 200

# Перемещение лейблов внутри окна
lx = 10  
y1 = 45
y2 = 105
y3 = 170

# шрифт для лейбла
front = "font: bold 12px"

# текст лейблов
label_from = "Path From: "
label_to = "Path To: "
label_Path = "Path: "
label_exe = "Exe: "


# размер радио-кнопок
rsize_x = 60
rsize_y = 30

# отступы радио-кнопок
xr1 = 10
xr2 = 65
xr3 = 120
yr = 7

# пути к иконкам
# ...


# расширения файлов
dat = '.dat'
txt = '.txt'
exe = '.exe'


# координаты линий редактирования 
xledit = 80
yledit_1 = 45
yledit_2 = 105



# размер линий
wl = 400

# координаты кнопок
xb = 490
yb1 = 43
yb2 = 105
yb3 = 155

# размеры кнопок
wb = 90
hb = 30

# названия кнопок
review = 'Обзор'
run = 'Выполнить'
move_ = "Move файлов"
exit_ = "Выход"

# выбор директорий 
select_dir = "Select Directory"


###########################
#-------> Pupo.py <-------#
###########################

#текстовые переменные для сообщений
delete_exe_str = "Удаление файлов"
rename_Out_res = "Переименование выходных файлов (Out_res.txt)"
delete_empty_dir = "Удаление пустых папок"


Warning = "Внимание!"
Message = "Сообщение "

#Название окна
Title = 'Cleaning program'

# Пути к иконкам
Icon = 'Icon.png'
Icon_play = 'Icon_play.png'
Icon_review = 'Icon_review.png'
Icon_copy = 'Icon_copy.png'
# расположение и размеры окна 
window_X = 600
window_Y = 300        

window_Width = 700
window_Height = 500

#------> Поля редактирования <------#

line_edit_wight = 580
line_edit_height = 30

line_edit_xy = 15

Text_X = 30
Text_Y = 190

Text_Wight = 640
Text_Height = 250

#------> Чек боксы <------#

exe_files_not_found = "Исполняемых файлов не найдено"
Out_res_not_found = "Out_res-файлов не найдено"
empty_dir_not_found = "Пустых директорий не найдено"

check_boxes_x = 20
check_box1_y = 60
check_box2_y = 90
check_box3_y = 120

check_boxes_wight = 400
check_boxes_height = 20

#------> Кнопки <------#
# название кнопок см. строку 73
btn_run_x = 570
btn_run_y = 450

btn_exit_x = 30
btn_exit_y = 450

btn_review_x = 600
btn_review_y = 15

btn_move_x = 580
btn_move_y = 150

btn_wight = 90
btn_height = 30

# название файла для поиска (.txt)
out_res = 'Out_res.txt'

first_row = ['Имя файла',
    'Высота',
    'Широта',
    'Долгота',
    'N',
    'E',
    'Период импульса',
    'Частота',
    ' ',
    'Фронт',
    'Спад',
    'Dll',
    'Глубина',
    ' ',
    'Rff']

# pyinstaller.exe --splash .\Icon_play.png .\Icon_copy.png .\Icon_review.png .\Icon.png -w -F --icon=Icon.ico Pupo.py

title_label_json = {
    'Radar: ': 10,
    'Mode: ': 35,
    'Channel: ': 60
}



