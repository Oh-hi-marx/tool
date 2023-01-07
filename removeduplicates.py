import os
import glob 
import hashlib

files = glob.glob("**/*",recursive=True)
files = [f for f in files if os.path.isfile(f)]
print(len(files))

exist = []
counter= 0
for file in files:
    if(file.split(os.sep)[-1] not in exist):
        exist.append(file.split(os.sep)[-1])
    else:
        counter+=1
print(exist)
print("removed %i duplicates" %counter)
