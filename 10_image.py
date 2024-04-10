from tkinter import *
from PIL import ImageTk

root = Tk()
root.title("coding block classes")
root.geometry("850x400+250+50")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

icon = ImageTk.PhotoImage(file='photos/background.png')

lbl = Label(root,image=icon)
lbl.place(x=0,y=0)

root.mainloop()