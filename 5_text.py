from tkinter import *
from tkinter import font
#root,window,master
root = Tk()
root.title("coding block class")
root.geometry("500x500+0+0")
# root.resizable(False,False)
img = PhotoImage(file='cb.png')
root.iconphoto(False,img)

#print(font.families())

#list=[]
def get_details() :
    #print(entry.get())
    print(txt.get('1.0',END))
    #result.config(text=str(entry.get()))
    # list.append(str(entry.get()))
    # result.config(text="\n".join(list))
    

lbl = Label(root,text="Tkinter Lecture",
            font=("times new roman",25,"bold"))
lbl.place(x=0,y=0,relwidth=1)

txt = Text(root,font=("times new roman",20,"bold"))
txt.place(x=0,y=100,width=200,height=100)

btn = Button(root,text="SHOW",font=("times new roman",20,"bold"),bg="grey",fg="red",
             activebackground="yellow",
             activeforeground="red",cursor="hand2",command=get_details)
btn.place(x=0,y=220,relwidth=1)

# result = Label(root,font=("times new roman",20,"bold"))
# result.place(x=0,y=220,relwidth=1)

root.mainloop()
