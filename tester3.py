import os
from PIL import Image,ImageFilter
dir = "../Dataset/UJTDchar/" # give home directory of dataset.
i=1
def do(filess):
    for files in filess:
        if files.endswith('.jpg'):
            img=Image.open(files)
            blur=img.filter(ImageFilter.BLUR)
            ee=img.filter(ImageFilter.EDGE_ENHANCE)
            contour=img.filter(ImageFilter.CONTOUR)
            detail=img.filter(ImageFilter.DETAIL)
            emboss=img.filter(ImageFilter.EMBOSS)
            smooth=img.filter(ImageFilter.SMOOTH)
            sharpen=img.filter(ImageFilter.SHARPEN)
            smooth_more=img.filter(ImageFilter.SMOOTH_MORE)
            ee.save("EEz"+str(i)+".jpg")
            blur.save("blsdur"+str(i)+".jpg")
            contour.save("cadsontour"+str(i)+".jpg")
            detail.save("deasftail"+str(i)+".jpg")
            emboss.save("emasdasboss"+str(i)+".jpg")
            smooth.save("smasdaooth"+str(i)+".jpg")
            sharpen.save("shsadarpen"+str(i)+".jpg")
            smooth_more.save("smooasdth_more_"+str(i)+".jpg")
for root, dirs, files in os.walk(dir):
    do(root)
    i+=1
