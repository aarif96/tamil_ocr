import os
from PIL import Image,ImageFilter
direc = "/Users/venkats/Desktop/UJTD/" # give home directory of dataset.
i=1
path = "/Users/venkats/Desktop/UJTD/"
files = os.listdir(path)
valid_images = [".jpg",".png"]
print(files)
for j,file in enumerate(files):
    if file!=".DS_Store":
        path1 = os.path.join(path,file)
        images = os.listdir(path1)
        count_per_class = 0
        for i,image in enumerate(images):
            print(i)
            ext = os.path.splitext(image)
            if ext[1].lower() in valid_images:
                img=Image.open(os.path.join(path1,image))
                blur=img.filter(ImageFilter.GaussianBlur(radius=0.3))
                ee=fil2=img.filter(ImageFilter.Kernel((3,3), [-1,-1,-1,-1,12,-1,-1,-1,-1]))
                contour=img.filter(ImageFilter.CONTOUR)
                detail=img.filter(ImageFilter.DETAIL)
                emboss=img.filter(ImageFilter.EMBOSS)
                smooth=img.filter(ImageFilter.SMOOTH)
                sharpen=img.filter(ImageFilter.Kernel((5, 5), [0,0,0,0,0,0,0,-1,0,0,0,-1,5,-1,0,0,0,-1,0,0,0,0,0,0,0]))
                smooth_more=img.filter(ImageFilter.SMOOTH_MORE)
                ee.save(path1 + "/EE"+str(i)+".jpg")
                blur.save(path1 + "/blur"+str(i)+".jpg")
                contour.save(path1 + "/contour"+str(i)+".jpg")
                detail.save(path1 + "/detail"+str(i)+".jpg")
                emboss.save(path1 + "/emboss"+str(i)+".jpg")
                smooth.save(path1 + "/smooth"+str(i)+".jpg")
                sharpen.save(path1 + "/sharpen"+str(i)+".jpg")
                smooth_more.save(path1 + "/smooth_more_"+str(i)+".jpg")
