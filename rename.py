import os
from os import listdir
from os.path import isfile, join
import shutil
import re


def onlyfiles(mypath):
	onlyfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles
path = input("path")
if(path == ""):
	path = "./"

files= onlyfiles(path)
print(len(files))

for file in files:
    f= file.split(".")[0]
    ext = file.split(".")[-1]
    f = file.zfill(11) + "." + ext
    print(file,f)
    #os.rename(file, f)
