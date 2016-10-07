###### Based on: http://stackoverflow.com/a/7589374/4929236 #####

import cv2
import numpy as np
import os

x = 0
dir_count = len([name for name in os.listdir('./pages') if os.path.isfile(name)])

for file in os.listdir("./pages"):
    if file.endswith(".jpg"):
        img = cv2.imread(file)
        if x > 0:
          if x+1 != dir_count:
            vis = np.concatenate((last_img, img), axis=0)
            cv2.imwrite('out.png', vis)
        last_img = img
        x += 1
