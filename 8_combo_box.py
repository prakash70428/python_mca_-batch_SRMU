from tkinter import *
from tkinter import ttk
#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

language = ttk.Combobox(root,values=("python","java","c++","c#","javaScript","kotlin","php"),
                        font=("times new roman",15,"bold"),state="readonly",justify=CENTER
                        )
language.place(x=10,y=10)

root.mainloop()
