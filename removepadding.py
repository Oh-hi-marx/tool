
import cv2
import glob
import os

import numpy as np
import shutil
path = "mu60"
file_list = glob.glob(path + "/*")
thresh = 10
for f in file_list:
    img = cv2.imread(f)
    hcount=0
    line = img[:,999-hcount:1000-hcount]
    print(img.shape)
    print(np.sum(line[0][0]-  line[500][0]))
    while(1):
        if(np.sum(line[0][0]-  line[500][0])< thresh  and np.sum(line[700][0] -line[999][0]) < thresh):
            hcount+=1
            line = img[:,999-hcount:1000-hcount]
        else:
            break
    img = img[:,0:1000-hcount]

    if(hcount==0):
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

        line = img[:,999-hcount:1000-hcount]

        while(1):
            if(np.sum(line[0][0]-  line[500][0])< thresh  and np.sum(line[700][0] -line[999][0]) < thresh):
                hcount+=1
                line = img[:,999-hcount:1000-hcount]
            else:
                break
        img = img[:,0:1000-hcount]
        print(hcount)
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imshow("", img)
    #cv2.waitKey(0)
    cv2.imwrite(path + "0" + os.sep + f.split(os.sep)[-1] + ".jpg", img)