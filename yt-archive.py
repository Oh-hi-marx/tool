from os import listdir
from os.path import isfile, join
mypath = "./"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print (onlyfiles)
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