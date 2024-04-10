from tkinter import *

#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

def get_data() :
    print(check_var.get())

check_var = StringVar()
check = Checkbutton(root,variable=check_var,text="Accept?Not",
                    onvalue="on",offvalue="off",font=("times new roman",15,"bold"))
check.place(x=10,y=10)
check_var.set("off")

btn = Button(root,text="SHOW",font=("times new roman",15,"bold"),command=check_var)
btn.place(x=10,y=50)

root.mainloop()
