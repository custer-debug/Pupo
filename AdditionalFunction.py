import os
from shutil import copyfile



def del_files(path:str,ex:str) -> str:
    count = 0
    for folder,_,files in os.walk(path):
        for _file in files:
            if _file.endswith(ex):
                os.remove(os.path.join(folder,_file))
                count += 1
    return f'{count} files delete'


def delete_empty_directories(path:str) -> int:
    result = 0
    for _dir in os.listdir(path):
        current_dir = os.path.join(path, _dir)
        if os.path.isdir(current_dir):
            result += int(delete_empty_directories(current_dir))
            if not os.listdir(current_dir):
                os.rmdir(current_dir)
                result += 1

    return result




def find_files(from_path:str) -> list:
    res = []
    for folder,_,files in os.walk(from_path):
        for f in files:
            if f.endswith('.txt'):
                res.append(os.path.join(folder,f))
    return res



def copy_files(from_path:str, to_path:str,cut_flag:bool = False) -> str:
    """Копирует файлы в указанный каталог

    Args:
        files (list): список файлов(абсолютный путь)
        to_path (str): конечный каталог

    Returns:
        int: количество скопированных файлов
    """

    files = find_files(from_path=from_path)
    for item in files:
            s = item.split('\\')
            tmp = os.path.join(
                to_path,
                ''.join([s[-2],'_',s[-1]]))
            copyfile(item,tmp)

    if cut_flag:
        del_files(from_path,'.txt')

    return "".join(['Файлы перемещены:\n',from_path,' -> ',to_path])


names = [
    'Имя файла',
    'Номер файла',
    'Номер импульса',
    'Широта',
    'Долгота',
    'N(UTM)',
    'E(UTM)',
    'T new',
    'delta T new',
    'Частота',
    'Фронт',
    'Спад',
    'Эпсилон (Dll)',
    'Глубина',
    'delta Freq',
    'Rff']


def remove_first_line(filename:str) -> None:
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        f.writelines(lines[1:])



def concatenate(files:list,output:str) -> str:
    with open(output,'a') as writter:
        writter.write('\t'.join(names) + '\n')
        for filename in files:
            tmp = filename.text()
            remove_first_line(tmp)
            with open(tmp,'r') as reader:
                for line in reader:
                    writter.write(line)
                reader.close()
        writter.close()

    return 'Файлы склеины'
