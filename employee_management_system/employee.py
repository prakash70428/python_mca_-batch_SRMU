from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Employee :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee management system")

        lbl_title = Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",
                          font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1330,height=50)
        
        # logo
        img_logo = Image.open('images/icon.jpg')
        img_logo = img_logo.resize((50,50))
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=170,y=0,width=50,height=50)

        #image frame
        img_frame = Frame(self.root,bd=2,relief='ridge',bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st image
        img1 = Image.open('images/img1.png')
        img1 = img1.resize((440,160))
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=440,height=160)

        # 2nd image
        img2 = Image.open('images/img3.png')
        img2 = img2.resize((440,160))
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame,image=self.photo2)
        self.img_2.place(x=420,y=0,width=440,height=160)

        # 3rd image
        img3 = Image.open('images/img2.png')
        img3 = img3.resize((440,160))
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame,image=self.photo3)
        self.img_3.place(x=850,y=0,width=440,height=160)

        # main frame
        Main_frame=Frame(self.root,bd=2,relief='ridge',bg='white')
        Main_frame.place(x=0,y=200,width=1350,height=560)

        # upper frame
        upper_frame = LabelFrame(Main_frame,bd=2,relief="ridge",bg='white',
                                 text='Employee Management Information',
                                 font=('arial',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1240,height=240)

        # down frame
        down_frame = LabelFrame(Main_frame,bd=2,relief="ridge",bg='white',
                                 text='Employee Management Information Table',
                                 font=('arial',11,'bold'),fg='red')
        down_frame.place(x=10,y=250,width=1240,height=240)


if __name__ == "__main__" :
    root = Tk()
    obj = Employee(root)
    root.mainloop()