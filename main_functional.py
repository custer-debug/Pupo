import os


def convert_bytes(size:float):
    if size < 0:
        return None
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


def delete_files(extension) -> int:
    size = 0
    count = 0
    for root, _, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(extension):
                path = os.path.join(root,file)
                # os.remove(path)
                size += os.stat(path).st_size
                count += 1
    return count



def find_first_file(extension:str, files:list) -> str:
    for item in files:
        if item.endswith(extension):
            return item
    return ''



def generate_new_name(root:str, txt:str, dat:str) -> str:
    return f'{root.split("/")[-1]} {txt.split(".")[0]}_{"_".join(dat.split("_")[1:6])}.txt'



def rename_files(cwd, name) -> None:
    for root, _, files in os.walk(cwd):
        dat =  find_first_file('.dat', files)
        txt =  find_first_file(name, files)
        if not txt: continue
        rename = generate_new_name(root,txt,dat)
        # os.rename(f'{root}/{txt}',f'{root}/{rename}')
        print(f'{root}/{txt} -> {rename}'.replace('\\','/'))






def delete_empty_directories(path:str) -> list[str]:
    remove = []
    for _dir in os.listdir(path):
        current_dir = os.path.join(path, _dir)
        if os.path.isdir(current_dir):
            delete_empty_directories(current_dir)
            if not os.listdir(current_dir):
                remove.append(current_dir)
                # os.rmdir(current_dir)
                # print()
    print(remove)
    return remove
# for i in os.walk(os.getcwd()): #root, folders, files
#     print([j for j in i[2] if j.endswith('.py')])
