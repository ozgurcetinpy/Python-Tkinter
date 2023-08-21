from tkinter import *

root = Tk()
root.title("Labels and Packes")
root.geometry("800x800")
root.resizable(0,0)
root.config(bg="blue")

label_name = Label(root, text = "Hello My name is Özgür ",fg = "White",bg= "Red")
label_name.pack()

label_name_2 = Label(root, text = "Helllo My Name is John",font=("Times", 18, "bold"))
label_name_2.pack()

label_name_3=Label(root)
label_name_3.config(text = " Hello my Name is Paul")
label_name_3.config(font = ("Cambria", 15))
label_name_3.pack(padx = 100, pady = 100)

label_name_4 = Label(root,text="Hello my name is Sue",bg="green",fg="purple")
label_name_4.pack(pady=(0,50),ipadx=100,ipady=50,anchor=W)

label_name_5 = Label(root,text="Hello my name is Pat",bg ="#ffffff",fg = "#123456")
label_name_5.pack(fill=Y,expand=True,padx = 10,pady=10)












root.mainloop()
