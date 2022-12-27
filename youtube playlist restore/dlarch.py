from os import listdir
from os.path import isfile, join
import os
import glob
def createDownloaded():
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
    
    
########
playlist = input("playlist?")
os.system('yt-dlp --force-write-archive -s --download-archive archive.txt ' + playlist)
createDownloaded()
########

downloaded = []
with open("downloaded.txt") as file:
    for line in file:
        downloaded.append(line.rstrip())
        
archive = []
with open("archive.txt") as file:
    for line in file:
        archive.append(line.rstrip())        
print("down", len(downloaded),len(archive))

final = []
for a in archive:
    if a not in downloaded:
        final.append(a)
print(len(final), "diff", len(archive) - len(final))

for i,f in enumerate(final):
    ytid = f.split("youtube ")[-1]
    print(i, len(final),ytid)
    cmd =  "yt-dlp "+ ytid + ' -f "bv*+ba/b" --restrict-filenames'
    os.system(cmd)