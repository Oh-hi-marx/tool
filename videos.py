
import os
import cv2
import numpy as np
def letterbox_image(image, expected_size):
    ih, iw, _ = image.shape
    eh, ew = expected_size
    scale = min(eh / ih, ew / iw)
    nh = int(ih * scale)
    nw = int(iw * scale)

    image = cv2.resize(image, (nw, nh), interpolation=cv2.INTER_CUBIC)
    new_img = np.full((eh, ew, 3), 128, dtype='uint8')
    # fill new image with the resized image and centered it
    new_img[(eh - nh) // 2:(eh - nh) // 2 + nh,
            (ew - nw) // 2:(ew - nw) // 2 + nw,
            :] = image.copy()
    return new_img
def extractFrames(inpath, outpath, resolution = (1080,1920)):
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
		  if(frame.shape[0:2]!=resolution):
			  frame = cv2.resize(frame, (resolution[1], resolution[0]))
		  cv2.imshow('Frame',frame)
		  cv2.imwrite(outpath+ "/" + str(counter)+".jpg", frame)
		  counter+=1
		  if cv2.waitKey(25) & 0xFF == ord('q'):
			  break
	  else:
      		break
	cap.release()
	cv2.destroyAllWindows()
