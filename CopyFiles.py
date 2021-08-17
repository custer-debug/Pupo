import shutil
import os

From = r"E:\ФЛЕШКА\Профили"
To = r"C:\Users\romak\Desktop\Pupo\Новая папка"

def splitName(str):
    return str.split('\\')[-1]

i = 1
for root, _, files in os.walk(From):
                for file in files:
                    if file.endswith(".txt"):
                        shutil.copyfile(root + "\\" + file, To + "\\" + splitName(root) + ".txt")
                        print(splitName(root))
                        #os.remove(root + "\\" + file)
                        

#original = r'C:\Users\r.krekoten\Desktop\Д.xlsx'
#target = r'C:\Users\r.krekoten\Desktop\Games\fds.xlsx'