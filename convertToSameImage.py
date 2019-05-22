import os
import cv2
import matplotlib.pyplot as plt

old_dir = 'data\cloud1'
new_dir = 'data\cloud2'
filename = 'pic0.png'

for i in range(len(os.listdir(old_dir))):
    path = os.path.join(old_dir,filename)
    im = cv2.imread(path,cv2.IMREAD_UNCHANGED)
    newPath = os.path.join(new_dir,'pic{}.png'.format(i))
    cv2.imwrite(newPath,im)