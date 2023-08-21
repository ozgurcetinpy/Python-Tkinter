from tkinter import *
from tkinter import ttk
from tkinter import END

#Define Window
root = Tk()
root.title("Metric Helper")
root.resizable(0,0)

#Define Fonts and Colors
field_font = ("Cambria",10)
bg_color = "#c75c5c"
button_color = "#f5cf87"
root.config(bg=bg_color)

#Define Functions
def Convert():
    metric_values = {
        "femto" : 10**-15,
        "pico" : 10**-12,
        "nano" : 10**-9,
        "micro" : 10**-6,
        "mili" : 10**-3,
        "santi" : 10**-2,
        "desi" : 10**-1,
        "ana birim" : 10**0,
        "deca" : 10**1,
        "hekta" : 10**2,
        "kilo" : 10**3,
        "mega" : 10**6,
        "giga" : 10**9,
        "tera" : 10**12,
        "peta" : 10**15
    }

    output_field.delete(0,END)

    start_value =float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    #Conver to the base unit first
    base_value = start_value * metric_values[start_prefix]
    #Convert to new metric Value
    end_value = base_value / metric_values[end_prefix]

    output_field.insert(0,str(end_value)) 



#Define Layout
#Create input and output entry fields
input_field = Entry(root,width=20,font=field_font,borderwidth=3)
output_field = Entry(root,width=20,font=field_font,borderwidth=3)
equal_label = Label(root,text="=",font=field_font,bg=bg_color)

input_field.grid(row=0,column=0,padx=10,pady=10)
equal_label.grid(row=0,column=1,pady=10,padx=10)
output_field.grid(row=0,column=2,padx=10,pady=10)

input_field.insert(0,"Enter Your Quantity")


#Create COMBOBOX for metric values
metric_list = ["famto","pico","nano","micro","mili","santi","desi","ana birim","deca","hekta","kilo","mega","giga","tera","peta"]

input_combobox = ttk.Combobox(root,value = metric_list, font=field_font, justify="center")
output_combobox = ttk.Combobox(root,value = metric_list, font=field_font, justify="center")
to_label = Label(root,text="to",font=field_font,bg=bg_color)

input_combobox.grid(row=1,column=0,padx=10,pady=10)
to_label.grid(row=1,column=1,pady=10,padx=10)
output_combobox.grid(row=1,column=2,padx=10,pady=10)

input_combobox.set("ana birim")
output_combobox.set("ana birim")


#Create a convert button
convert_button = Button(root,bg=button_color,text="Convert",font=field_font,command=Convert)
convert_button.grid(row=2,column=1,pady=10,padx=10,ipadx=50)



root.mainloop()