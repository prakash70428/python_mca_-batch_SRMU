from tkinter import *

#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

def get_gender() :
    print(gender.get())

gender = StringVar()
lbl = Label(root,text="select gender:",font=("times new roman",15,"bold"))
lbl.place(x=0,y=0)
male = Radiobutton(root,text="MALE",value="male",font=("times new roman",15,"bold"),variable=gender)
male.place(x=10,y=50)
female = Radiobutton(root,text="FEMALE",value="female",variable=gender,font=("times new roman",15,"bold"))
female.place(x=10,y=100)

gender.set("male")

btn = Button(root,text="SHOW",font=("times new roman",15,"bold"),command=get_gender)
btn.place(x=10,y=150)

root.mainloop()
