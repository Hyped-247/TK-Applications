from tkinter import *
from tkinter import messagebox


root = Tk().withdraw()  # hiding the main window
var = messagebox.askyesno("Title", "Your question goes here?")

filename = "log.txt"

f = open(filename, "w")
f.write(str(var))
print(str(var) + " has been written to the file " + filename)
f.close()