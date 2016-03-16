# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 20:49:11 2015

@author: SyamPrasad
"""

#import pylshbox
import numpy as np
from lshash import LSHash
#import Image
from PIL import Image
#import cv
image_size = []
dataset = "C:/Users/SyamPrasad/Desktop/fall 2015/data mining/assignment/assignment4/Images/dataset/"
queryset = "C:/Users/SyamPrasad/Desktop/fall 2015/data mining/assignment/assignment4/Query/"
fileext = ".bmp"

img = Image.open(dataset+"1"+fileext)
#pixel = np.array(img)
#shape = pixel.shape
#onedarray = pixel.ravel()
#image_size = onedarray
#vector = np.matrix(onedarray)
big_array=[]
image_number=[]

#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#hist,bins = np.histogram(pixel.ravel(),256,[0,256])

lsh = LSHash(3, 255)
for x in range(1, 100000):
    img = Image.open(dataset+str(x)+fileext)
    pixel = np.array(img)
    #onedarray = pixel.ravel()
    hist,bins = np.histogram(pixel.ravel(),256,[0,256])
    listing=list(hist[0:255])
    big_array.append(listing)
    lsh.index(listing)

input_array=np.array(big_array)

img = Image.open(queryset+"10"+fileext)
pixel = np.array(img)
#onedarray = pixel.ravel()
hist,bins = np.histogram(pixel.ravel(),256,[0,256])
listing=list(hist[0:255])
k=lsh.query(listing,distance_func="l1norm")
vector = np.matrix(k)
length=len(k)
if length > 0:
    for output in range(length):
        if (k[output][1] < 800):
            test=np.array(k[output][0])
            result=np.where((input_array == test).all(axis=1))
            image_number.append(result[0][0]+1)
        
        #arr2 = np.asarray(k[output][0]).reshape(shape)
        #vector = np.matrix(np.uint8(arr2))
        #img2 = Image.fromarray(np.uint8(arr2),'RGB')
        #img2.show()
 #onedarray = pixel.ravel()
 #image_size.append[x]=onedarray
 
#shape = arr.shape
#final_image = np.asarray(vector).reshape(shape)