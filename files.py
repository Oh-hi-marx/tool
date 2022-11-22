import os
from os import listdir
from os.path import isfile, join
import shutil
	
def onlyfiles(mypath):
	onlyfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles
	
def onlyfolders(mypath):
	return next(os.walk(mypath))[1]
	
def removeAllFiles(mypath):
	shutil.rmtree(mypath)
