import os
import cv2
import numpy as np
path = "/Users/apple/Downloads/UJTDcharactersnew/" ##### replace this
files = os.listdir(path)
print(files)
x = []
y = []
count = []
valid_images = [".jpg",".gif",".png",".tga"]
dim = (32,32)
for i,file in enumerate(files):
    if file!=".DS_Store":
        path1 = os.path.join(path,file)
        images = os.listdir(path1)
        count_per_class = 0
        for image in images:
            # path2 = os.path.join(path1,image)
            ext = os.path.splitext(image)
            if ext[1].lower() in valid_images:

                
                img = cv2.imread(os.path.join(path1,image),0)
                if img.shape[0]<32 or img.shape[1]<32:
                    count_per_class+=1
                #print(img.shape)
                img_resize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                img_chan = np.expand_dims(img_resize,axis=2)
                x.append(img_chan)
                y.append(i)
        print(len(x),i)
        count.append(count_per_class)


    

x = np.array(x)
y = np.array(y)
print(count)
print(x.shape,y.shape)


    