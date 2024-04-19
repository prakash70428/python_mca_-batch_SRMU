from tkinter import *

#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

Frame1 = Frame(root,bd=2,relief="ridge")
Frame1.place(x=250,y=50,height=300,width=200)

scrolly = Scrollbar(Frame1,orient=VERTICAL)
scrolly.pack(side=RIGHT,fill=Y)

data = Listbox(Frame1,font=('times new roman',20),justify=CENTER,yscrollcommand=scrolly.set)
data.pack()
scrolly.config(command=data.yview)
for i in range(0,101) :
    data.insert(i,"Student: " + str(i))

root.mainloop()
