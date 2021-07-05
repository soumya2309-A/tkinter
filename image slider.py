from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("images app")

my_img1=ImageTk.PhotoImage(Image.open('G:\hi.png '))
my_img2=ImageTk.PhotoImage(Image.open('G:\star3.png'))
my_img3=ImageTk.PhotoImage(Image.open('G:\heart.png'))
my_img4=ImageTk.PhotoImage(Image.open('G:\str.png'))


my_lst=[my_img1,my_img2,my_img3,my_img4]
status=Label(root,text="image 1 of"+str(len(my_lst)),bd=1,relief=SUNKEN,anchor=E)

my_label=Label(image=my_img4)

my_label.grid(row=0,column=0,columnspan=3)


def forward(img_number):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    my_label=Label(image=my_lst[img_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_number+1))
    button_back = Button(root, text="<<", command=lambda: back(img_number-1))
    if img_number==4:
        button_forward = Button(root, text=">>",state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="image" + str(img_number) + "of" + str(len(my_lst)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(img_number):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    my_label=Label(image=my_lst[img_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_number+1))
    button_back = Button(root, text="<<", command=lambda: back(img_number-1))

    if img_number==1:
        button_back = Button(root, text="<<",state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back=Button(root,text="<<",command=back,state=DISABLED)
button_exit=Button(root,text="Exit",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()