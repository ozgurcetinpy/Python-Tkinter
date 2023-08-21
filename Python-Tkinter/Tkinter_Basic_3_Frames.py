from tkinter import *
from tkinter import BOTH

root = Tk()
root.title("Window Basic 3")
root.geometry("500x500")
root.resizable(0,0)


pack_frame = Frame(root,bg="red")
grid_frame_1 = Frame(root,bg="blue")
grid_frame_2 = LabelFrame(root,text="Grid System Rules!",borderwidth=5)

#pack Frame
pack_frame.pack(fill=BOTH,expand=True)
grid_frame_1.pack(fill=X,expand=True)
grid_frame_2.pack(fill=BOTH,expand=True,padx=10,pady=10)

#pack Frame
Label(pack_frame,text="text").pack()
Label(pack_frame,text="text").pack()
Label(pack_frame,text="text").pack()

#grid_frame_1
Label(grid_frame_1,text="text").grid(row=0,column=0)
Label(grid_frame_1,text="text").grid(row=1,column=1)
Label(grid_frame_1,text="text").grid(row=2,column=2)
#Label(grid_frame_1,text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row=3,column=0)

#grid_frame_2
Label(grid_frame_2,text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row=0,column=0)










root.mainloop()