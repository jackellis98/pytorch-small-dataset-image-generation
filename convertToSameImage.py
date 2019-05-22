import os
import cv2
import matplotlib.pyplot as plt

old_dir = 'data\cloud1'
new_dir = 'data\cloud2'
filename1 = 'pic0.png'
filename2 = 'pic3.png'

for i in range(len(os.listdir(old_dir))):
    if i<25:
        path = os.path.join(old_dir,filename1)
        im = cv2.imread(path,cv2.IMREAD_UNCHANGED)
        newPath = os.path.join(new_dir,'pic{}.png'.format(i))
        cv2.imwrite(newPath,im)
    else:
        path = os.path.join(old_dir,filename2)
        im = cv2.imread(path,cv2.IMREAD_UNCHANGED)
        newPath = os.path.join(new_dir,'pic{}.png'.format(i))
        cv2.imwrite(newPath,im)