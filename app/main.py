from tkinter import *
import cv2
from cv2 import imread
import PIL.Image, PIL.ImageTk

global photo
global cv_image
global entry_L
global canvas
def read_image():

    cv_image = imread(entry_L.get())
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_image))
    canvas.create_image(0, 0, image=photo, anchor=NW)


root = Tk()
root.title('Model Definition')

root.geometry('{}x{}'.format(460, 350))

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")


# create the widgets for the top frame
model_label = Label(top_frame, text='Model Dimensions')
entry_L = Entry(top_frame, background="orange",width=50)
btn_image=Button(top_frame, text="open", command=read_image)

# layout the widgets in the top frame
entry_L.grid(row=0,column=0,sticky='nswe' )
btn_image.grid(row=0,column=1, columnspan=3,sticky='nswe')

top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)


# create the center widgets
center.grid_rowconfigure(1, weight=1)
center.grid_columnconfigure(0, weight=1)

ctr_left = Frame(center, bg='blue', width=275, height=190,padx=3, pady=3)
ctr_right = Frame(center, bg='green', width=275, height=190, padx=3, pady=3)

ctr_left.pack(side=LEFT,fill='both', expand=True)
ctr_right.pack(side = RIGHT,fill='both', expand=True)

canvas = Canvas(ctr_left)
canvas.pack(fill='both', expand=True)

ctr_right_TOP= Frame(ctr_right, bg='green', width=275, height=95, padx=3, pady=3)
ctr_right_BOTTOM = Frame(ctr_right, bg='red', width=275, height=95, padx=3, pady=3)

ctr_right_TOP.pack(side=TOP,fill='both', expand=True)
ctr_right_BOTTOM.pack(side = TOP,fill='both', expand=True)

#reads an input image 
 

# # Callback for the "Blur" button


#     photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_image))
#     canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

# # find frequency of pixels in range 0-255 
# histr = calcHist([cv_image],[0],None,[256],[0,256]) 
# gray = cvtColor(cv_image, COLOR_BGR2GRAY)

# # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
# height, width, no_channels = cv_image.shape
# # Create a canvas that can fit the above image
# canvas = tkinter.Canvas(window, width = width, height = height)
# #canvas.pack()

# # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
# photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_image))

# # Add a PhotoImage to the Canvas
# canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
# # Button that lets the user blur the image
# btn_blur=tkinter.Button(top_frame, text="Blur", command=blur_image)
# #btn_blur.pack(side=LEFT, expand=True)
# #imshow('Original image',image)
# #imshow('Gray image', gray)
# Run the window loop
root.mainloop()