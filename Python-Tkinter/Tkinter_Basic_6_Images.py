from tkinter import *


root = Tk()
root.title("Image")
root.iconbitmap("Ico.png")
root.geometry("700x700")
root.resizable(0,0)

my_ımage = PhotoImage(file="Ico.png")
my_label = Label(root,image=my_ımage)
my_label.pack()

my_button = Button(root,image=my_ımage)
my_button.pack()


lion_image = PhotoImage(file="Lion.jpg")
lion_label = Label(root,image=lion_image)
lion_label.pack()



root.mainloop()