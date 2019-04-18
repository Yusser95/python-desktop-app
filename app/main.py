from tkinter import *
from cv2 import imread,calcHist,cvtColor,COLOR_BGR2GRAY
import PIL.Image, PIL.ImageTk ,PIL.ImageOps
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
def read_image():
    global photo
    global cv_image
    global entry_L
    global canvas_LEFT
    global canvas_RIGHT_BOTTOM
    global canvas_RIGHT_UP
    global f1
    global f2
    global toolbar1

    #read image
    path = filedialog.askopenfilename()
    cv_image = imread(path)

    #set enray_l
        
    #create image 
    gray = cvtColor(cv_image, COLOR_BGR2GRAY)
    w,h=canvas_LEFT.winfo_width(),canvas_LEFT.winfo_height()
    image = PIL.Image.fromarray(gray)
    image = PIL.ImageOps.fit(image, (w,h), PIL.Image.ANTIALIAS)
    photo = PIL.ImageTk.PhotoImage(image)   
    canvas_LEFT.create_image(0, 0, image=photo, anchor=NW)
    
    #create hisogram
    p1=f1.gca()
    p1.hist(cv_image.ravel(),256,[0,256])
    canvas_RIGHT_UP._tkcanvas.pack()

    # create pie chart
    labels = ['red', 'Blue', 'green', 'orang']
    sizes = [15, 30, 45, 10]
    ##add colors
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    ax2=f2.gca()
    ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ## Equal aspect ratio ensures that pie is drawn as a circle
    ax2.axis('equal')
    canvas_RIGHT_BOTTOM.draw()



root = Tk()
root.title('Model Definition')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h-(h*0.1)))

# create all of the main containers
top_frame = Frame(root,  width=450, height=50, pady=3)
center = Frame(root,  width=50, height=40, padx=3, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")


# create the widgets for the top frame
entry_L = Entry(top_frame, width=40)
btn_image=Button(top_frame, text="open", command=read_image, width=10)

# layout the widgets in the top frame
entry_L.grid(row=0,column=0,sticky='nswe' )
btn_image.grid(row=0,column=1, columnspan=3,sticky='nswe')
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)


# create the center widgets
ctr_left = Frame(center,  width=275, height=190)
ctr_right = Frame(center,  width=275, height=190)
ctr_left.pack(side=LEFT,fill='both', expand=True)
ctr_right.pack(side = RIGHT,fill='both', expand=True)


# create the center_left widgets
canvas_LEFT = Canvas(ctr_left)
canvas_LEFT.pack(fill='both', expand=True)

# create the center_Right widgets
ctr_right_TOP= Frame(ctr_right,  width=275, height=95)
ctr_right_BOTTOM = Frame(ctr_right,  width=275, height=95)
ctr_right_TOP.pack(side=TOP,fill='both', expand=True)
ctr_right_BOTTOM.pack(side = BOTTOM,fill='both', expand=True)

# create the center_Right_Top widgets
f1 = Figure(figsize=(2,2))
canvas_RIGHT_UP =FigureCanvasTkAgg(f1,ctr_right_TOP)
canvas_RIGHT_UP.get_tk_widget().pack(fill='both', expand=True)
toolbar1 = NavigationToolbar2Tk(canvas_RIGHT_UP,ctr_right_TOP)
canvas_RIGHT_UP.draw()
toolbar1.update()

# create the canvas_RIGHT_BOTTOM widgets
f2 = Figure(figsize=(2,2))
canvas_RIGHT_BOTTOM =FigureCanvasTkAgg(f2,ctr_right_BOTTOM)
canvas_RIGHT_BOTTOM.get_tk_widget().pack(fill='both', expand=True)
toolbar2 = NavigationToolbar2Tk(canvas_RIGHT_BOTTOM,ctr_right_BOTTOM)
canvas_RIGHT_BOTTOM.draw()
toolbar2.update()


# find frequency of pixels in range 0-255 
##histr = calcHist([cv_image],[0],None,[256],[0,256]) 


## Get the image dimensions (OpenCV stores image data as NumPy ndarray)
##height, width, no_channels = cv_image.shape
root.mainloop()