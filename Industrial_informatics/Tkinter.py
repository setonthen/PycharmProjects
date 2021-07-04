from tkinter import *

root =Tk()

# defining the window widget
mylabel1 = Label(root, text = 'hello world!')
mylabel2 = Label(root, text = "My name is Joshua")
mylabel3 = Label(root, text = "            ")  #this is used not necessarily to create space or
                                                # indentation between mylabel1 and my lable2


mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=5)
mylabel3.grid(row=1, column=1)

# shoving it to the screen
# mylabel11.pack()
# mylabel12.pack()



root.mainloop()

