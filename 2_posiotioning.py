from tkinter import *
from tkinter import font

#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

# f = font.families()
# print(f)

#--------grid--------
# lb1 = Label(root,text="Hello world 1",font=("Script",30,"bold"))
# lb1.grid(row=0,column=0)

# lb2 = Label(root,text="Hello world 2",font=("Script",30,"bold"))
# lb2.grid(row=0,column=1)

# lb3 = Label(root,text="Hello world 3",font=("Script",30,"bold"))
# lb3.grid(row=2,column=0)

#-------------------pack--------
# lb1 = Label(root,text="Hello world 1",font=("Script",30,"bold"))
# lb1.pack(side=LEFT)

# lb2 = Label(root,text="Hello world 2",font=("Script",30,"bold"),bg="red")
# lb2.pack(expand=1,fill=BOTH)

# lb3 = Label(root,text="Hello world 3",font=("Script",30,"bold"))
# lb3.pack()

# lb4 = Label(root,text="Hello world 4",font=("Script",30,"bold"))
# lb4.pack(side=BOTTOM)

#--------------place-----------------
lb1 = Label(root,text="Hello world 1",font=("Script",30,"bold"))
lb1.place(x=0,y=0)

lb2 = Label(root,text="Hello world 2",font=("Script",30,"bold"))
lb2.place(x=200,y=200)

lb3 = Label(root,text="Hello world 3",font=("Script",30,"bold"))
lb3.place(x=400,y=400)


root.mainloop()
