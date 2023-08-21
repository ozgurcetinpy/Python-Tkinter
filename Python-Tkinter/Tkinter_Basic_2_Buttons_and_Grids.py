from tkinter import *

root = Tk()
root.title("Windows Basic 2")
root.geometry("500x500")
root.resizable(0,0)


button_name_1= Button(root,text="Name")
button_name_1.grid(row=0,column=0)

button_name_2 = Button(root,text="Time")
button_name_2.grid(row=0,column=1)

button_name_3 = Button(root,text="Place",bg="#00ffff",activebackground="#ff0000")
button_name_3.grid(row=0,column=2,padx=20,pady=20,ipadx=40)

button_name_4 = Button(root,text="Day",fg="White",bg="Black",borderwidth=5)
button_name_4.grid(row=1,column=0,columnspan=3,sticky=EW)


test_buttom_1 = Button(root,text="test")
test_buttom_2 = Button(root,text="test")
test_buttom_3 = Button(root,text="test")
test_buttom_4 = Button(root,text="test")
test_buttom_5 = Button(root,text="test")
test_buttom_6 = Button(root,text="test")

test_buttom_1.grid(row=2,column=0,pady=5,padx=5)
test_buttom_2.grid(row=2,column=1,pady=5,padx=5)
test_buttom_3.grid(row=2,column=2,pady=5,padx=5,sticky=W)
test_buttom_4.grid(row=3,column=0,pady=5,padx=5)
test_buttom_5.grid(row=3,column=1,pady=5,padx=5)
test_buttom_6.grid(row=3,column=2,pady=5,padx=5,sticky=W)


root.mainloop()