import os
import shutil
import logging

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
        size /= 1024.0,x

    return (size,' byte')

def delete_files(files) -> tuple[int,int]:
    size = 0
    for item in files:
        size += os.stat(item).st_size
        try:
            os.remove(item)
        except Exception:
            logging.error('Exception', exc_info=True)
            return (files.index(item),size)
    return (len(files),size)

def find_first_file(endswitch:str, files:list) -> str:
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

def find_all_files_extension(cwd:str, extension:str) -> list[str]:
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

def send_out_files(cwd:str,path_exe:str) -> None:
    """Функция из главного функционала.
    Выполняет рассылку исполняемых файлов по папкам.

    Args:
        cwd (str): корневой каталог
        path_exe (str): путь к файлу
    """
    exe = path_exe.split('/')[-1]
    for root,folders,_ in os.walk(cwd):
        for folder in folders:
            to = os.path.join(root, folder,exe)
            try:
                shutil.copyfile(path_exe,to)
                # self.Print(self.area, os.path.join(root, folder,exe))
            except Exception as e:
                print(e)
                logging.error('Exception', exc_info=True)
                return

def copy_files(files:list, to_path:str):
    for item in files:
        try:
            shutil.copyfile(item,os.path.join(to_path,item.split('\\')[-1]))
        except Exception as e:
            print(e)


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
                    ' ',
                    'Глубина',
                    ' ',
                    'Rff'
                ]
    except Exception:
        logging.error('Exception', exc_info=True)

# print(type(add_cap(r'C:\Users\r.krekoten\Desktop\Эксперимент 08.12.21\3\3_2021_12_08_12_result.txt')))
