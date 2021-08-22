import shutil
import os


for root, folders, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(".txt"):
                    os.rename(root + "\\" + file, root + "\\" + "Out_res.txt")




for root, folders, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(".txt"):
                    shutil.copy(r"C:\Users\romak\Desktop\raw_2021_07_23_07_39_55.644.dat", root + "\\" + "raw_2021_07_23_07_39_55.644.dat" )


for root, folders, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(".txt"):
                    shutil.copy(r"C:\Users\romak\Desktop\X7OscarLite_V2020.1103.exe", root + "\\" + "X7OscarLite_V2020.1103.exe" )




#C:\Users\romak\Desktop\X7OscarLite_V2020.1103.exe

