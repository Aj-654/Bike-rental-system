from tkinter import *
import PIL as pillow
from PIL import Image,ImageTk

class admin:
    def __init__(self,root):
        self.root = root
        self.root.title("Admin Page")
        self.root.geometry("1920x1080")
        img1=Image.open(r"D:\SEM4 MINI PROJECT\startbg2.png")
        self.photoimg1= ImageTk.PhotoImage(img1)
        
        lblimg=Label(self.root,image=self.photoimg1)
        lblimg.place(x=0,y=0,relheight=1,relwidth=1)
        

if __name__=="__main__":
    root=Tk()
    obj=admin(root)
    root.mainloop()