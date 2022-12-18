import os
from os import listdir
from os.path import isfile, join
import shutil
import re


def onlyfiles(mypath):
	onlyfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles
path = input("path: ")


files= onlyfiles(path)
print(len(files))

for file in files:
	base = file.split(os.sep)[0]
	f= file.split(".")[0].split(os.sep)[-1]
	ext = file.split(".")[-1]
	final = base+ os.sep + f.zfill(11) + "." + ext
	print(file,final)
	os.rename(file, final)
