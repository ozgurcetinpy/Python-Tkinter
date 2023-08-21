from tkinter import *
from tkinter import END


root = Tk()
root.title("Again")
root.geometry("500x500")
root.resizable(0,0)


def MakeLabel():
    label_1 = Label(output_frame,text= text_entry.get())
    label_1.pack()
    text_entry.delete(0,END)

def CountDown(number):
    global value
    count_label = Label(output_frame,text=value)
    count_label.pack()
    value = number + 1



input_frame = Frame(root,bg="Blue",width=500,height = 150)
output_frame = Frame(root,bg="Red",width=500, height = 350)
input_frame.pack(padx=5,pady=5)
output_frame.pack(pady=5,padx=5)


text_entry = Entry(input_frame,width=20)
text_entry.grid(row = 0, column = 0, padx=5,pady=5,ipadx=40)
input_frame.grid_propagate(0)

input_button = Button(input_frame,text= "Print",command=MakeLabel)
input_button.grid(row=0,column=1,ipadx=30)


value = 0
count_button = Button(input_frame,text="Count",width=40,height=2,command=lambda:CountDown(value))
count_button.grid(row=1,column=0,pady=5,padx=5,columnspan=20)


root.mainloop()
