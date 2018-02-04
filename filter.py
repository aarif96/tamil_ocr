import os
from PIL import Image,ImageFilter
direc = "/Users/apple/Downloads/UJTDcharactersnew/" # give home directory of dataset.
i=1

path = "/Users/apple/Downloads/UJTDcharactersnew copy/" ##### replace this
files = os.listdir(path)
valid_images = [".jpg",".gif",".png",".tga"]
print(files)
for ii,file in enumerate(files):
    if file!=".DS_Store":
        path1 = os.path.join(path,file)
        images = os.listdir(path1)
        count_per_class = 0
        for i,image in enumerate(images):
            print(i)
            # path2 = os.path.join(path1,image)
            ext = os.path.splitext(image)
            if ext[1].lower() in valid_images:

                
                # img = cv2.imread(os.path.join(path1,image),0)
                # if img.shape[0]<32 or img.shape[1]<32:
                #     count_per_class+=1
                #print(img.shape)
                img=Image.open(os.path.join(path1,image))
                blur=img.filter(ImageFilter.BLUR)
                ee=img.filter(ImageFilter.EDGE_ENHANCE)
                contour=img.filter(ImageFilter.CONTOUR)
                detail=img.filter(ImageFilter.DETAIL)
                emboss=img.filter(ImageFilter.EMBOSS)
                smooth=img.filter(ImageFilter.SMOOTH)
                sharpen=img.filter(ImageFilter.SHARPEN)
                smooth_more=img.filter(ImageFilter.SMOOTH_MORE)
                ee.save(path1 + "/EEz"+str(i)+".jpg")
                blur.save(path1 + "/blsdur"+str(i)+".jpg")
                contour.save(path1 + "/cadsontour"+str(i)+".jpg")
                detail.save(path1 + "/deasftail"+str(i)+".jpg")
                emboss.save(path1 + "/emasdasboss"+str(i)+".jpg")
                smooth.save(path1 + "/smasdaooth"+str(i)+".jpg")
                sharpen.save(path1 + "/shsadarpen"+str(i)+".jpg")
                smooth_more.save(path1 + "/smooasdth_more_"+str(i)+".jpg")
                # img_resize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                # img_chan = np.expand_dims(img_resize,axis=2)
                
        


# def do(filess):
#  for files in os.listdir(filess):
#   print(filess)
#   if files.endswith('.jpg'):
#    img=Image.open(os.path.join(files,filess))
#    blur=img.filter(ImageFilter.BLUR)
#    ee=img.filter(ImageFilter.EDGE_ENHANCE)
#    contour=img.filter(ImageFilter.CONTOUR)
#    detail=img.filter(ImageFilter.DETAIL)
#    emboss=img.filter(ImageFilter.EMBOSS)
#    smooth=img.filter(ImageFilter.SMOOTH)
#    sharpen=img.filter(ImageFilter.SHARPEN)
#    smooth_more=img.filter(ImageFilter.SMOOTH_MORE)
#    ee.save("EEz"+str(i)+".jpg")
#    blur.save("blsdur"+str(i)+".jpg")
#    contour.save("cadsontour"+str(i)+".jpg")
#    detail.save("deasftail"+str(i)+".jpg")
#    emboss.save("emasdasboss"+str(i)+".jpg")
#    smooth.save("smasdaooth"+str(i)+".jpg")
#    sharpen.save("shsadarpen"+str(i)+".jpg")
#    smooth_more.save("smooasdth_more_"+str(i)+".jpg")


# # print("ghi")
# print(os.walk(direc))

# classes = os.path.jo
# for root, dirs, files in os.walk(direc):
#   print(root)
#   do(root)
#   i+=1