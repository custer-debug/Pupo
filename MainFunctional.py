import os
import shutil
import logging
import collections
# from time import sleep



def convert_bytes(size:int) -> tuple[int,int]:
    """Функция определения единиц измерения по размеру удалённых файлов.\n
    Возрвращает единицы измерения и округлённый до целых размер удалённых файлов.

    Args:
        size (int): размер файл -а/-ов в байтах

    Returns:
        tuple[int,str]: округленный до целого размер и единица измерения
    """
    for x in ['байтов', 'Кб', 'Мб', 'Гб', 'Тб']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return (size,' byte')

def delete_files(files:list) -> tuple[int,int]:
    size = 0
    for item in files:
        size += os.stat(item).st_size
        try:
            os.remove(item)
        except Exception:
            return (files.index(item),size)
    return (len(files),size)

def find_first_file(endswitch:str = '.txt', files:list = None) -> str:
    """Функция выбора первого файла из списка.
    Файлы ищутся с определённым расширением.

    Args:
        endswitch (str): расширение
        files (list[str]): список строк файлов

    Returns:
        str: найденный файл
    """
    for file in files:
        if file.endswith(endswitch):
            return file
    return ''

def find_all_files_extension(cwd:str = os.getcwd(), extension:str = '.txt') -> list[str]:
    """Функция поиска файлов по расширению.
    Возрващает список строк.
    Одна строка - это полный путь к файлу.

    Args:
        cwd(str): путь к папке
        extension(str): расширение

    Returns:
        list[str]: найденные файлы
    """

    files_list = []
    for root, _, files in os.walk(cwd):
        for item in files:
            if item.endswith(extension):
                files_list.append(os.path.join(root,item))
    return files_list

def copy_files(files:list, to_path:str) -> int:
    """Копирует файлы в указанный каталог

    Args:
        files (list): список файлов(абсолютный путь)
        to_path (str): конечный каталог

    Returns:
        int: количество скопированных файлов
    """
    for count,item in enumerate(files):
        try:
            tmp = os.path.join(to_path,item.split('\\')[-1])
            print(tmp)
            shutil.copyfile(item,tmp)

        except Exception as e:
            print(e)
            return count

    return len(files)

def add_cap(item:str) ->list[str]:
    try:
        with open(item.text(),'r') as f:
            if len(f.readline().split('\t')) == 2:
                return [
                    'Дальность, м',
                    'Амплитуда']
            else:
                return [
                    'Название файла',
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
                    'Rff'
                ]
    except Exception:
        logging.error('Exception', exc_info=True)

def same_files(files:list) -> tuple[int,int]:
    """Проверяет количество одинаковых файлов в подпапках

    Args:
        files (list): список файлов, абсолютный путь

    Returns:
        tuple[int,int]: количество повторов и общее количество файлов
    """
    tmp = [item.split('\\')[-1] for item in files]
    y = collections.Counter(tmp)
    count = 0
    for it,item in enumerate(y.items()):
        if item[1] > 1:
            count = it + 1
    return (len(files),count)
