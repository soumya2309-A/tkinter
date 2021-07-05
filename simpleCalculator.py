from tkinter import *

root=Tk()
root.title("simple calulator")


myentry=Entry(root,width=40,borderwidth=4)
myentry.grid(row=0,column=0,columnspan=4,padx=10,pady=15)

def buttonClick(number):
    current=myentry.get()
    myentry.delete(0,END)
    myentry.insert(0,str(current)+ str(number))

def buttonClear():
    myentry.delete(0, END)

def buttonAdd():
    first_number=myentry.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    myentry.delete(0, END)


def buttonEqual():
    second_number = myentry.get()
    myentry.delete(0, END)

    if math=="addition":
        myentry.insert(0,f_num + int(second_number))
    if math == "subtraction":
        myentry.insert(0, f_num - int(second_number))
    if math == "multiplication":
        myentry.insert(0, f_num * int(second_number))
    if math == "division":
        myentry.insert(0, f_num / int(second_number))

def buttonSub():
    first_number = myentry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    myentry.delete(0, END)

    return

def buttonMul():
    first_number = myentry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    myentry.delete(0, END)

    return

def buttonDiv():
    first_number = myentry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    myentry.delete(0, END)

    return
#define buttons

button1=Button(root,text="1",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(1))
button2=Button(root,text="2",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(2))
button3=Button(root,text="3",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(3))
button4=Button(root,text="4",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(4))
button5=Button(root,text="5",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(5))
button6=Button(root,text="6",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(6))
button7=Button(root,text="7",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(7))
button8=Button(root,text="8",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(8))
button9=Button(root,text="9",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(9))
button0=Button(root,text="0",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=lambda:buttonClick(0))
buttonA=Button(root,text="+",fg="black",borderwidth=3,bg="lightcyan",padx=29,pady=10,command=buttonAdd)
buttonS=Button(root,text="-",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=buttonSub)
buttonM=Button(root,text="*",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=buttonMul)
buttonD=Button(root,text="/",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=buttonDiv)
buttonE=Button(root,text="=",fg="black",borderwidth=3,bg="lightcyan",padx=30,pady=10,command=buttonEqual)
buttonC=Button(root,text="Clear",fg="black",borderwidth=3,bg="mistyrose",padx=106,pady=10,command=buttonClear)



#put my button on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonA.grid(row=4,column=1)
buttonS.grid(row=4,column=2)
buttonM.grid(row=5,column=1)
buttonD.grid(row=5,column=2)
buttonE.grid(row=5,column=0)
buttonC.grid(row=6,column=0,columnspan=3)

root.mainloop()