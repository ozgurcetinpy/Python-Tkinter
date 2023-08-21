from tkinter import *
from tkinter import IntVar, StringVar

#Define Window
root = Tk()
root.title("Win Basic")
root.geometry("350x350")
root.resizable(0,0)


def MakeLabel():
    if number.get() == 1:
        num_label = Label(output_frame,text="1 one 1")
    elif number.get() == 2:
        num_label = Label(output_frame,text="2 two 2")
    num_label.pack()


#Define Frames
input_frame = LabelFrame(root,text="This is fun",width=350,height=100)
output_frame = Frame(root,width=350,height=250)
input_frame.pack(padx=10,pady=10)
output_frame.pack(padx=10,pady=(0,10))

#Define Widgets
number = IntVar()   # Bu yapılmalı  
radio_1 = Radiobutton(input_frame, text="print the number one",variable=number,value=1)  # Değişkeni number , değeri 1
radio_2 = Radiobutton(input_frame, text="Print the number two",variable=number,value=2)
print_button = Button(input_frame, text="Print the Number",command=MakeLabel)


#Define Radio Buttons
radio_1.grid(row=0,column=0,pady=10,padx=10)
radio_2.grid(row=0,column=1,pady=10,padx=10)
print_button.grid(row=1,column=0,columnspan=2,padx=10,pady=10)   # Ortalamak için



root.mainloop()