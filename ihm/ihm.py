from tkinter import *

OPTIONS = [
"Janvier",
"Février",
"Mars",
"Avril",
"Mai",
"Juin",
"Juillet"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

mainloop()