import os
import cv2
import matplotlib.pyplot as plt

old_dir = 'data\cloud'
new_dir = 'data\cloud'

for filename in os.listdir(old_dir):
    path = os.path.join(old_dir,filename)
    im = cv2.imread(path,cv2.IMREAD_UNCHANGED)
    channels = cv2.split(im)
    newIm = cv2.bitwise_not(channels[3])
    newIm = cv2.cvtColor(newIm,cv2.COLOR_GRAY2RGB)
    newIm = newIm[0:600, 0:700] #Cropping noun-project authors
    finalIm = cv2.resize(newIm, (50, 50)) 
    newPath = os.path.join(new_dir,filename)
    cv2.imwrite(newPath,finalIm)