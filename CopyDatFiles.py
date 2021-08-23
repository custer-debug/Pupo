import os
import shutil
import time
cwd = os.getcwd()

d = dict()


def findContinue(search,root):
    print(search)
    for r, _, files in os.walk(root):
        for file in files:
            if file.startswith(search):
                shutil.move(f"{r}\\{file}", f"{cwd}\\{file}")
                print(f"{r}\\{file}" + " ---> " + f"{cwd}\\{file}")


def splitDate(str):
    s = str.split('_')
    s.pop(0)
    a = s[-1].split('.')
    s.pop(-1)
    s.append(a[0])
    return int(s[-1])


def generateFindName(name, second):
    s = name.split('_')
    s.pop(-1)
    if second < 10:
        return '_'.join(s) + "_0" + str(second)
    
    return '_'.join(s) + "_" + str(second)
    


def fileSequence(file, root):
    d[splitDate(file)] = file
    if len(d) > 1:
        l = list(d.keys())[-2] + 1 
        r = list(d.keys())[-1]
        if  l != r:
            findContinue(generateFindName(file, l), root)
            return True
    return False


def startMoveFiles():
    d.clear()
    for file in os.listdir(cwd):
        if file.endswith(".dat") and fileSequence(file, cwd):
            startMoveFiles()


startMoveFiles()
d.clear()