from tkinter import *


def sel(val):
	selection = None
	if var.get():
		selection = "Value = " + str(var.get())
	selection = val
	label.config(text=selection)


root = Tk()
var = DoubleVar()
scale = Scale(root, variable=var, command=sel)
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value",  command=lambda : sel(scale.get()))
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()