import os

l = []



for root, folders, files in os.walk(os.getcwd()):
    l=files
    for file in files:
        if file.endswith(".dat") and len(folders) != 0:
            print(file)    
            break
print(l)

