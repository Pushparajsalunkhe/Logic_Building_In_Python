from tkinter import *
def btnclick(n):
    if(n==1):
        mf["bg"]="red"
    elif(n==2):
        mf["bg"]="green"
    elif(n==3):
        mf["bg"]="blue"
    elif(n==4):
        mf["bg"]="black"
    elif(n==5):
        mf["bg"]="pink"
myroot=Tk()
myroot.geometry("700x700")
myroot.title("Student section")
myroot.wm_iconbitmap(r"C:\Users\patil\Pictures\Saved Pictures\salunkhe.jpeg")
mf=Frame(myroot,width=700,height=700,bg="#FF6103",cursor="cross")
mf.propagate(0)
mf.pack()
btnred=Button(mf,width=12,height=2,text="red color",bg="red",fg="white",command=lambda : btnclick(1))
btngreen=Button(mf,width=12,height=2,text="greeen color",bg="green",fg="white",command=lambda : btnclick(2))
btnblue=Button(mf,width=12,height=2,text="blue color",bg="blue",fg="white",command=lambda : btnclick(3))
btnblack=Button(mf,width=12,height=2,text="black color",bg="black",fg="white",command=lambda : btnclick(4))
btnpink=Button(mf,width=12,height=2,text="pink color",bg="pink",fg="white",command=lambda:btnclick(5))
btnred.pack()
btngreen.pack()
btnblue.pack()
btnblack.pack()
btnpink.pack()
myroot.mainloop()
