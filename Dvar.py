##############################
#-------> CopyWindow <-------#
##############################
from os import cpu_count
# количество частей разбиения dat-файлов
SPLIT_NUM = cpu_count()

# сообщения об успешном или ошибочном ты программы
ERROR_FROM_VALUE = "Необходимо выбрать первый путь"
ERROR_TO_VALUE   = "Необходимо выбрать второй путь"
ERROR_FILE_PATH_VALUE = "Выберите файл"
TITLE_WINDOW_ERROR   = "Ошибка"
TITLE_WINDOW_SUCCESSFUL = "Успех"
MSG_SUCCESSFUL_COPY = "Файлы скопированы"
MSG_SUCCESSFUL_SPLIT = "Файлы успешно разделены"

MSG_START_COPY = "Начало копирования"
MSG_FINISH_COPY = "Конец копирования"

# название окна
TITLE_COPY = 'Copy txt'
TITLE_SPLITE = 'Split dat'
TITLE_SEND_OUT = 'Send out exe'

# координаты расположения окна
WIN_X = 400
WIN_Y = 200

# размер окна
WIN_WIDHT = 600
WIN_HEIGHT = 210
WIN_HEIGHT_NEW = 270


# Перемещение лейблов внутри окна
X_LABEL = 10
Y_LABEL_1 = 45
Y_LABEL_2 = Y_LABEL_1 + 60  #150
Y_LABEL_3 = Y_LABEL_1 + 125 #170

# шрифт для лейбла
FRONT_LABEL_TITLE = "font: bold 12px"

# текст лейблов
LABEL_FROM = 'Path From:'
LABEL_TO = 'Path To:'
LABEL_PATH = 'Path:'
LABEL_EXE = 'Exe:'
LABEL_JSON = 'Json: '


# размер радио-кнопок
RADIO_SIZE_WIDHT = 85
RADIO_SIZE_HEIGHT = 30

# отступы радио-кнопок
X_RADIO_BUTTON_1 = 10
X_RADIO_BUTTON_2 = X_RADIO_BUTTON_1 + RADIO_SIZE_WIDHT #65
X_RADIO_BUTTON_3 = X_RADIO_BUTTON_2 + RADIO_SIZE_WIDHT #120
X_RADIO_BUTTON_4 = X_RADIO_BUTTON_3 + RADIO_SIZE_WIDHT + 20 #120

Y_RADIO_BUTTON = 10


# расширения файлов
DAT = '.dat'
TXT = '.txt'
EXE = '.exe'

COLLECT_DAT = 'Collect dat'
COLLECT_TXT = 'Collect txt'
SEND_OUT_EXE = 'Send out exe'
SPLIT_DAT = 'Split dat'

# координаты линий редактирования
X_LINE_EDIT = 80
Y_LINE_EDIT_1 = 45
Y_LINE_EDIT_2 = Y_LINE_EDIT_1 + 60 #105
Y_LINE_EDIT_3 = Y_LINE_EDIT_2 + 60 #165

# размер линий
LINE_WIDHT = 400
# высота линий редактирования см. линии редактирования главного окна


# координаты кнопок
X_BUTTON = 490
Y_BUTTON_1 = 43
Y_BUTTON_2 = Y_BUTTON_1 + 62 #105
Y_BUTTON_3 = Y_BUTTON_2 + 60 #155

# размеры кнопок
WIDHT_BUTTON = 90
HEIGHT_BUTTON = 30

# названия кнопок
TITLE_REVIEW = 'Обзор'
TITLE_RUN = 'Выполнить'
TITLE_MOVE = 'Move файлов'
TITLE_EXIT = 'Выход'
TITLE_CONFIG = 'Config file'
# выбор директорий
SELECT_DIRECTORY = "Select Directory"


###########################
#-------> Pupo.py <-------#
###########################

#Сообщения
MSG_DELETE_FILES = "Удаление файлов"
MSG_RENAME_FILES = "Переименование файлов"
MSG_DELETE_EMPTY_DIR = "Удаление пустых папок"


# Message = "Сообщение "

#Название окна
TITLE_MAIN_WINDOW = 'Cleaning program'

# расположение и размеры окна
WINDOW_X = 600
WINDOW_Y = 300

WINDOW_WIDHT = 700
WINDOW_HEIGHT = 500

#------> Поля редактирования <------#

MAIN_LINE_EDIT_WIDHT = 580
MAIN_LINE_EDIT_HEIGHT = 30

LINE_EDIT_XY = 15

LINE_EXTENSION_X = 140
LINE_EXTENSION_Y = 57
LINE_EXTENSION_WIDHT = 50
LINE_EXTENSION_NAMEFILE_HIEGHT = 25

LINE_NAMEFILE_X = 175
LINE_NAMEFILE_Y = 90
LINE_NAMEFILE_WIDHT = 80



TEXT_FIELD_X = 30
TEXT_FILED_Y = 190

TEXT_FILED_WIDHT = 640
TEXT_FILED_HEIGHT = 250

#------> Чек боксы <------#

MSG_FILES_NOT_FOUND = "Искомых файлов не найдено"
MSG_EMPTY_DIR_NOT_FOUND = "Пустых директорий не найдено"

CHECK_BOXES_X = 20
CHECK_BOX_Y1 = 60
CHECK_BOX_Y2 = CHECK_BOX_Y1 + 30
CHECK_BOX_Y3 = CHECK_BOX_Y2 + 30

CHECK_BOXES_WIGHT = 400
CHECK_BOXES_HEIGHT = 20

#------> Кнопки <------#

BUTTON_RUN_X = 570
BUTTON_RUN_Y = 450

BUTTON_EXIT_X = 30
BUTTON_EXIT_Y = 450

BUTTON_REVIEW_X = 600
BUTTON_REVIEW_Y = 15

BUTTON_MOVE_X = 580
BUTTON_MOVE_Y = 150

# btn_wight = 90
# btn_height = 30

# название файла для поиска (.txt)
OUT_RES = 'Out_res.txt'

FIRST_ROW = ['Имя файла',
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


TITLE_JSON_LABEL = {
    'Radar: ': 10,
    'Mode: ': 35,
    'Channel: ': 60
}


SIZE = [
    'Byte',
    'Kilobyte',
    'Megabyte',
    'Gigabyte'
    'Terabyte'
]

# имя резльтирующего xslx-файла
XSLX_NAME_FILE = 'Res.xslx'

MSG_ERROR_PARAM = 'Выберите все нужные параметры'
MSG_SUCCESSFUL_SAVE = 'Файл успешно сохранён'
WINDOW_CONFIG_COORDINATE = 500
WINDOW_CONFIG_SIZE = 300


Text = ''
