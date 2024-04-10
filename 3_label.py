from tkinter import *

#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

lb1 = Label(root,text="Hello world 1",font=("Script",30,"bold"),bg="red")
lb1.pack(fill=X)

lb2 = Label(root,text="Hello world 2",font=("Script",30,"bold"),bg="red",
            fg="yellow",bd=10,relief="groove",pady=10)
lb2.pack(fill=X,pady=20,padx=20)

lb3 = Label(root,text="Hello world 3",font=("Script",30,"bold"),bg="red")
lb3.pack(fill=X)
 
root.mainloop()
