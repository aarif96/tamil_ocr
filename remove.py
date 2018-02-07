from PIL import Image
import cv2
import os

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk("./binarized"):
    for filename in filenames:
        if filename.endswith('.jpg'):
            list_of_files[filename] = os.sep.join([dirpath, filename])


for file in list_of_files:
    im = Image.open("./binarized/"+file)
    pixels = im.getdata()          # get the pixels as a flattened sequence
    black_thresh = 126
    nblack = 200
    for pixel in pixels:
      if pixel < black_thresh:
          nblack += 1
    n = len(pixels)

    if (nblack / float(n)) > 0.9:
       print("mostly black "+file)
       try:
         os.remove("./binarized/"+file)
       except: pass
    if (nblack/float(n)<0.05):
       print("mostly white "+file)
       try:
          os.remove("./binarized/"+file)
       except: pass

