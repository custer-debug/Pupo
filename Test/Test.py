import os
import shutil

def make_directories():
    for i in range(10):
        To = f"{cwd}\Part_{str(i+1)}"
        os.makedirs(To)
        shutil.copy(exe,To + "\SignalProc.exe")



def split_files(files,num): 
    size = len(files)
    for i in range(10):
        for _ in range(num[i]):
            file = files[0]
            From =  f"{file[0]}\\{file[1]}"
            To  = f"{file[0]}\\Part_{i+1}\\{file[1]}"
            shutil.move(From,To)
            files.remove(files[0])
            print(f"Success: {len(files)} / {size}")
         
        

cwd =  os.getcwd()
exe = r"D:\Repos\Pupo\Test\SignalProc.exe"
files = []
files_list = []
for root, dirs, files in os.walk(cwd):  
    for file in files:
        if file.endswith(".dat") and file not in [f[1] for f in files_list]:
            files_list.append([root, file])


Count_files = len(files_list)
split_num = []
for i in range(10):
    split_num.append(Count_files // 10)
split_num[-1] += Count_files % 10


make_directories()
split_files(files_list,split_num)