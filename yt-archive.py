from os import listdir
import glob
import os
mypath = "./"
onlyfiles = glob.glob(os.getcwd()+ os.sep +"*")
print (len(onlyfiles))
final = []

for f in onlyfiles:
    start = f.rfind("[")
    end = f.rfind("]")
    if(start != -1 and end != -1):
        final.append(f[start+1:end])
print(final)

f = open("downloaded.txt", "w")

for a in final:
    txt = "youtube "+ a + "\n"
    f.write(txt)
f.close()