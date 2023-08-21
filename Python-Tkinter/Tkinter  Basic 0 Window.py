import tkinter 

root = tkinter.Tk()
root.title("Window Basics")
root.geometry("250x500")
root.resizable(0,1)
root.config(bg="Green")

top = tkinter.Toplevel()
top.title("Second Window")
top.config(bg="#123")
top.geometry("200x200+500+50")

root.mainloop()
