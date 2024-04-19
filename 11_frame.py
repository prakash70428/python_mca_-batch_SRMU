from tkinter import *

#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

window = Frame(root,bg="lightgray",bd=10,relief="groove")
window.place(x=50,y=50,height=340,width=450)

show=Button(window,text='show',bg='green',font=('times new roman',15,'bold')).place(x=50,y=50)
show=Button(window,text='show',bg='green',font=('times new roman',15,'bold')).place(x=250,y=50)
show=Button(window,text='show',bg='green',font=('times new roman',15,'bold')).place(x=50,y=150)

window1 = LabelFrame(root,text='Employee Management System',font=('times new roman',15,'bold'))
window1.place(x=550,y=50,height=340,width=450)

root.mainloop()
