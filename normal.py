from tkinter import *

root = Tk()
root.geometry("1000x800")
root.title("Sports Bike")

options_frame = Frame(root,bg='lightblue')

options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=200,height=900)

home_btn = Button(options_frame,text='Honda Shine',font=('Bold',15),fg='#158aff',bd=0)
home_btn.place(x=10,y=50)

main_frame = Frame(root)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=500)

mainloop()