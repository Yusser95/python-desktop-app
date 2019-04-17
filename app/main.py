from tkinter import *

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

# layout the widgets in the top frame
entry_L.grid(row=0,column=0,sticky='nswe' )
model_label.grid(row=0,column=1, columnspan=3,sticky='nswe')

top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_columnconfigure(0, weight=1)


# create the center widgets
center.grid_rowconfigure(1, weight=1)
center.grid_columnconfigure(0, weight=1)

ctr_left = Frame(center, bg='blue', width=275, height=190,padx=3, pady=3)
#ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg='green', width=275, height=190, padx=3, pady=3)
#ctr_left.place(relheight=1,relwidth=1,anchor='e')
#ctr_right.place(relheight=1,relwidth=1,anchor='w')
#ctr_left.grid(row=0, column=0, sticky="ns")
#ctr_mid.grid(row=0, column=1, sticky="nsew")
#ctr_right.grid(row=0, column=1, sticky="ns")

ctr_left.pack(side=LEFT,fill='both', expand=True)
ctr_right.pack(side = RIGHT,fill='both', expand=True)

ctr_right_TOP= Frame(ctr_right, bg='green', width=275, height=95, padx=3, pady=3)
ctr_right_BOTTOM = Frame(ctr_right, bg='red', width=275, height=95, padx=3, pady=3)

ctr_right_TOP.pack(side=TOP,fill='both', expand=True)
ctr_right_BOTTOM.pack(side = TOP,fill='both', expand=True)


root.mainloop()