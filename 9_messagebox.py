from tkinter import *
from tkinter import messagebox

#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

def message1() :
    messagebox.showerror("ShowError","This is show error message")

def message2() :
    messagebox.showinfo("ShowInfo","This is show info message")  

def message3() :
    messagebox.showwarning("ShowWarning",'This is show warning error')   

btn1 = Button(root,text="message1",font=("times new roman",10,"bold"),command=message1)
btn1.place(x=50,y=50,width=100,height=40)
btn2 = Button(root,text="message2",font=("times new roman",10,"bold"),command=message2)
btn2.place(x=170,y=50,width=100,height=40)
btn3 = Button(root,text="message3",font=("times new roman",10,"bold"),command=message3)
btn3.place(x=280,y=50,width=100,height=40)

root.mainloop()
