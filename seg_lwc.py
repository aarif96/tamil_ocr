import cv2
import numpy as np
import copy
import os

# import the necessary packages
import numpy as np
 
# import the necessary packages

# Malisiewicz et al.
def non_max_suppression_fast(boxes, overlapThresh):
	# if there are no boxes, return an empty list
	if len(boxes) == 0:
		return []

	# if the bounding boxes integers, convert them to floats --
	# this is important since we'll be doing a bunch of divisions
	if boxes.dtype.kind == "i":
		boxes = boxes.astype("float")

	# initialize the list of picked indexes	
	pick = []

	# grab the coordinates of the bounding boxes
	x1 = boxes[:,0]
	y1 = boxes[:,1]
	x2 = boxes[:,2]
	y2 = boxes[:,3]

	# compute the area of the bounding boxes and sort the bounding
	# boxes by the bottom-right y-coordinate of the bounding box
	area = (x2 - x1 + 1) * (y2 - y1 + 1)
	idxs = np.argsort(y2)

	# keep looping while some indexes still remain in the indexes
	# list
	while len(idxs) > 0:
		# grab the last index in the indexes list and add the
		# index value to the list of picked indexes
		last = len(idxs) - 1
		i = idxs[last]
		pick.append(i)

		# find the largest (x, y) coordinates for the start of
		# the bounding box and the smallest (x, y) coordinates
		# for the end of the bounding box
		xx1 = np.maximum(x1[i], x1[idxs[:last]])
		yy1 = np.maximum(y1[i], y1[idxs[:last]])
		xx2 = np.minimum(x2[i], x2[idxs[:last]])
		yy2 = np.minimum(y2[i], y2[idxs[:last]])

		# compute the width and height of the bounding box
		w = np.maximum(0, xx2 - xx1 + 1)
		h = np.maximum(0, yy2 - yy1 + 1)

		# compute the ratio of overlap

		overlap = (w * h) / area[idxs[:last]]

		# delete all indexes from the index list that have
		idxs = np.delete(idxs, np.concatenate(([last],
			np.where(overlap > overlapThresh)[0])))

	# return only the bounding boxes that were picked using the
	# integer data type
	return boxes[pick].astype("int")

# Malisiewicz et al.
# def non_max_suppression_fast(boxes, overlapThresh):
# 	# if there are no boxes, return an empty list
# 	if len(boxes) == 0:
# 		return []
 
# 	# if the bounding boxes integers, convert them to floats --
# 	# this is important since we'll be doing a bunch of divisions
# 	if boxes.dtype.kind == "i":
# 		boxes = boxes.astype("float")
 
# 	# initialize the list of picked indexes	
# 	pick = []
 
# 	# grab the coordinates of the bounding boxes
# 	print(boxes.shape)  #print(len(boxes),len(boxes[0]),len(boxes[0][0]))
# 	x1 = boxes[:,0]
# 	y1 = boxes[:,1]
# 	x2 = boxes[:,2]
# 	y2 = boxes[:,3]
 
# 	# compute the area of the bounding boxes and sort the bounding
# 	# boxes by the bottom-right y-coordinate of the bounding box
# 	area = (x2 - x1 + 1) * (y2 - y1 + 1)
# 	idxs = np.argsort(y2)
 
# 	# keep looping while some indexes still remain in the indexes
# 	# list
# 	while len(idxs) > 0:
# 		# grab the last index in the indexes list and add the
# 		# index value to the list of picked indexes
# 		last = len(idxs) - 1
# 		i = idxs[last]
# 		pick.append(i)
 
# 		# find the largest (x, y) coordinates for the start of
# 		# the bounding box and the smallest (x, y) coordinates
# 		# for the end of the bounding box
# 		xx1 = np.maximum(x1[i], x1[idxs[:last]])
# 		yy1 = np.maximum(y1[i], y1[idxs[:last]])
# 		xx2 = np.minimum(x2[i], x2[idxs[:last]])
# 		yy2 = np.minimum(y2[i], y2[idxs[:last]])
 
# 		# compute the width and height of the bounding box
# 		w = np.maximum(0, xx2 - xx1 + 1)
# 		h = np.maximum(0, yy2 - yy1 + 1)
 
# 		# compute the ratio of overlap
# 		overlap = (w * h) / area[idxs[:last]]
 
# 		# delete all indexes from the index list that have
# 		idxs = np.delete(idxs, np.concatenate(([last],
# 			np.where(overlap > overlapThresh)[0])))
 
# 	# return only the bounding boxes that were picked using the
# 	# integer data type
# 	return boxes[pick].astype("int")

################ Line Segmentation
idx = 0
image = cv2.imread("/Users/apple/PycharmProjects/OCR/tam_book.png",0)

Kernel = np.ones((5,250),np.uint8)
im = copy.copy(image)
im1 = copy.copy(image)
ret,thresh = cv2.threshold(im,127,255,0)
thresh = cv2.bitwise_not(thresh)
im = cv2.dilate(thresh, Kernel, iterations=1)
cv2.imwrite("/Users/apple/PycharmProjects/OCR/contours/line_dilated.jpg",im)
#print(im)

im2,contours,hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
contours = np.array(contours)
#contours = non_max_suppression_fast(contours,overlapThresh=0.5)
# cv2.drawContours(im1,contours,-1,(0,255,0),3)
# cv2.imwrite("/Users/apple/PycharmProjects/OCR/line_contours.jpg",im1)

lstBb = []
for cnt in contours:
    lstBb.append(cv2.boundingRect(cnt))

cntbb = [(c,b) for (c,b) in zip(contours,lstBb)]
# cntbb = sorted(cntbb, key=lambda x: x[1][0])
cntbb = sorted(cntbb, key=lambda x: x[1][1])
cnts = []
cnts = [c for c,b in cntbb]
bb = np.array([b for c,b in cntbb])

for x,y,w,h in bb:
    roi = image[y-3 : y+h+3, x-3 : x+w+3]
    cv2.rectangle(im1,(x-3,y-3),(x+w+3,y+h+3),(0,255,0),2)
    if roi.any():
        cv2.imwrite("/Users/apple/PycharmProjects/OCR/segmented/line" + str(idx) + ".jpg",roi)       
    idx+=1
cv2.imwrite("/Users/apple/PycharmProjects/OCR/char_contours.jpg",im1)

# f.close()
#i+=1

#############   Word Segmentation
idx = 0
path_segments = '/Users/apple/PycharmProjects/OCR/segmented/line3.jpg'
img = cv2.imread(path_segments,0)
Kernel = np.ones((6,11),np.uint8)
im = copy.copy(img)
im1 = copy.copy(img)
ret,thresh = cv2.threshold(im,127,255,0)
thresh = cv2.bitwise_not(thresh)
im = cv2.dilate(thresh, Kernel, iterations=1)
cv2.imwrite("/Users/apple/PycharmProjects/OCR/contours/dilate_word1.jpg",im)
im2,contours,hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#contours = non_max_suppression_fast(contours,overlapThresh=0.5)

# cv2.drawContours(im1,contours,-1,(0,255,0),3)
# cv2.imwrite("/Users/apple/PycharmProjects/OCR/word_contours.jpg",im1)

lstBb = []
for cnt in contours:
    lstBb.append(cv2.boundingRect(cnt))

cntbb = [(c,b) for (c,b) in zip(contours,lstBb)]
cntbb = sorted(cntbb, key=lambda x: x[1][0])
# cntbb = sorted(cntbb, key=lambda x: x[1][1])
cnts = []
cnts = [c for c,b in cntbb]
bb = np.array([b for c,b in cntbb])
for x,y,w,h in bb:
    roi = img[y-3 : y+h+3, x-3 : x+w+3]
    cv2.rectangle(im1,(x-3,y-3),(x+w+3,y+h+3),(0,255,0),2)
    if roi.any():
        cv2.imwrite("/Users/apple/PycharmProjects/OCR/segmented/word" + str(idx) + ".jpg",roi)       
    idx+=1
cv2.imwrite("/Users/apple/PycharmProjects/OCR/char_contours.jpg",im1)

# cv2.imwrite("/Users/apple/PycharmProjects/OCR/contours/words.jpg",im1)

# line_segments = os.listdir(path_segments)
# ij = 0
# for seg in line_segments:
#     img = cv2.imread(os.path.join(path_segments,seg),0)
#     Kernel = np.ones((1,5),np.uint8)
#     im = copy.copy(img)
#     ret,thresh = cv2.threshold(im,127,255,0)
#     thresh = cv2.bitwise_not(thresh)
#     print(img.shape)
#     im = cv2.dilate(thresh, Kernel, iterations=1)
#     cv2.imwrite("/Users/apple/PycharmProjects/OCR/contours/word" + str(ij) + '.jpg',thresh)

#     ij+=1

################Character segmentation
img = cv2.imread("/Users/apple/PycharmProjects/OCR/segmented/word0.jpg",0)


Kernel = np.ones((6,1),np.uint8)
im = copy.copy(img)
im1 = copy.copy(img)
ret,thresh = cv2.threshold(im,127,255,0)
thresh = cv2.bitwise_not(thresh)
im = cv2.dilate(thresh, Kernel, iterations=1)

cv2.imwrite("/Users/apple/PycharmProjects/OCR/contours/dilate_char1.jpg",im)
im2,contours,hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# contour_sup = []
# for i in contours:
#     contour_t = []
#     for j in i:
#         for k in j:
#             contour_t.append(k)
#     contour_sup.append(contour_t)

# print(contour_sup)
# contours = np.array(contour_sup)

#contours = non_max_suppression_fast(contours,overlapThresh=0.5)
contours = np.array(contours)
#cv2.drawContours(im1,contours,-1,(0,255,0),3)

bbl = []
for cnt in contours:
    bbl.append(cv2.boundingRect(cnt))
lstBb = np.array(bbl)
#lstBb = non_max_suppression_fast(bbl,overlapThresh=1.0)
# print(lstBb)

cntbb = [(c,b) for (c,b) in zip(contours,lstBb)]
cntbb = sorted(cntbb, key=lambda x: x[1][0])
# cntbb = sorted(cntbb, key=lambda x: x[1][1])
cnts = []
cnts = [c for c,b in cntbb]
bb = np.array([b for c,b in cntbb])
idx = 0
for x,y,w,h in bb:
    roi = img[y-3 : y+h+3, x-3 : x+w+3]
    cv2.rectangle(im1,(x-3,y-3),(x+w+3,y+h+3),(0,255,0),2)
    if roi.any():
        cv2.imwrite("/Users/apple/PycharmProjects/OCR/segmented/char" + str(idx) + ".jpg",roi)       
    idx+=1
cv2.imwrite("/Users/apple/PycharmProjects/OCR/char_contours.jpg",im1)

# cv2.imwrite("/Users/apple/PycharmProjects/OCR/contours/words.jpg",im1)

