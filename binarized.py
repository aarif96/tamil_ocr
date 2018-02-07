import cv2
import os

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk("./segmented"):
    for filename in filenames:
        if filename.endswith('.jpg'):
            list_of_files[filename] = os.sep.join([dirpath, filename])

id=0
for file in list_of_files:
    img= cv2.imread("./segmented/"+file,0)
    ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imwrite("./binarized/binarized"+str(id)+".jpg",thresh)
    id+=1


