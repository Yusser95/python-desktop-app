import tkinter

# importing library for plotting 
from matplotlib import pyplot as plt 
# importing required libraries of opencv 

import cv2
from cv2 import imread,calcHist,cvtColor,imshow,COLOR_BGR2GRAY

# Create a window
window = tkinter.Tk()
  
# reads an input image 
image = imread('flower.jpg') 
 
# find frequency of pixels in range 0-255 
histr = calcHist([image],[0],None,[256],[0,256]) 
gray = cvtColor(image, COLOR_BGR2GRAY)

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = image.shape
# Create a canvas that can fit the above image
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=image, anchor=tkinter.NW)

#imshow('Original image',image)
#imshow('Gray image', gray)
# Run the window loop
window.mainloop()