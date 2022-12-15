
import os
import cv2
import numpy as np
import moviepy.editor as mp
from files import *
def letterbox_image(image, size):
    '''resize image with unchanged aspect ratio using padding'''
    iw, ih = image.shape[0:2][::-1]
    w, h = size
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)
    image = cv2.resize(image, (nw,nh), interpolation=cv2.INTER_CUBIC)
    new_image = np.zeros((size[1], size[0], 3), np.uint8)
    new_image.fill(128)
    dx = (w-nw)//2
    dy = (h-nh)//2
    new_image[dy:dy+nh, dx:dx+nw,:] = image
    return new_image
def extractFrames(inpath, outpath, resolution = (1080,1920), letterBox =0):
	# Create a VideoCapture object and read from input file
	# If the input is the camera, pass 0 instead of the video file name

	cap = cv2.VideoCapture(inpath)

	# Check if camera opened successfully
	if (cap.isOpened()== False):
	  print("Error opening video stream or file")

	# Read until video is completed
	counter=0
	while(cap.isOpened()):
	  # Capture frame-by-frame
	  ret, frame = cap.read()
	  if ret == True:
		  if(frame.shape[0:2]!=resolution and letterBox ==1):
			  frame = letterbox_image(frame, [1920,1080])
		  #cv2.imshow('Frame',frame)
		  cv2.imwrite(outpath+ "/" + str(counter)+".jpg", frame)
		  counter+=1
		  #if cv2.waitKey(25) & 0xFF == ord('q'):
		#	  break
	  else:
      		break
	cap.release()
	cv2.destroyAllWindows()

def renderFromFrames(framesPath,outputPath="", framespersecond=30, outputName = "", video = ""):
    if(video!=""):
        my_clip = mp.VideoFileClip(video)
        framespersecond = my_clip.fps
        my_clip.audio.write_audiofile("tempExtactedAudio.wav")
    try:
        os.mkdir(outputPath)
    except:
        pass
    if(outputName==""):
        outputName= framesPath.split(os.sep)[-1]
    cwd = os.getcwd()
    files = onlyfiles(framesPath)
    for f in files:
        name = f.split(os.sep)[-1].split(".")[0]
        padded = name.zfill(11)
        extension = f.split(".")[-1]
        directory = os.sep.join(f.rsplit(os.sep)[0:-1])
        #print(directory +os.sep+ padded + "."+extension)
        os.rename(f,directory + os.sep+  padded +"."+ extension )
    command = "ffmpeg -framerate "+ str(framespersecond)+" -thread_queue_size 1024 -i "
    command +=  framesPath + os.sep + '%011d.' + extension+ ' ' +cwd+os.sep +outputPath+ os.sep+ outputName  +".mp4"
    if(video!=""):
        command += " -i tempExtactedAudio.wav"

    print(command)
    os.system(command)
    if(video!=""):
        os.remove("tempExtactedAudio.wav")

extractFrames("NzishIREebw.webm", "testt")
renderFromFrames("testt",video = "NzishIREebw.webm")#, video = "C1zuQ4AgACU.webm")
