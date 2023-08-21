from tkinter import *
from tkinter import END

root = Tk()
root.title("Entry Basics!")
root.geometry("500x500")
root.resizable(0,0)


def MakeLabel():
    text = Label(output_frame,text=text_entry.get())
    text.pack()
    text_entry.delete(0,END)

def CountUp(number):
    """ Count up on the App"""
    global value

    text = Label(output_frame, text=number,bg="#ff0000")
    text.pack()
    value = number + 1

input_frame = Frame(root,bg="#0000ff",width=500,height=100)        
output_frame = Frame(root,bg="#ff0000",width=500,height=400)    
input_frame.pack(padx=10,pady=10)
output_frame.pack(padx=10,pady=(0,10))                                                                # Frames must be expanded! 

text_entry = Entry(input_frame,width=40)
text_entry.grid(row=0,column=0,pady=5,padx=5)
input_frame.grid_propagate(0)   

print_button = Button(input_frame,text="Print",command=MakeLabel)
print_button.grid(row=0,column=1,ipadx=30)

value = 0
count_button = Button(input_frame,text="count",command=lambda:CountUp(value))
count_button.grid(row=1,column=0,sticky="WE",columnspan=2, padx=10,pady=10)



root.mainloop()