# Introduction to programming
# Muhammad Ali Gulzar
# Converting feets into inches


from tkinter import *
from tkinter import ttk


# function that will convert the feet unit to inches unit
def calculate():
    try:
        value = float(feet.get())
        meters.set(format((0.3048 * value * 10000.0 + 0.5) / 10000.0,".5f"))
    except ValueError:
        pass

# the main window of the program
root = Tk()

# the title of the window
root.title("Feet to Meters")

# dividing the window in sections
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# variables to store the input given by the user
feet = StringVar()
meters = StringVar()

# adding entry widgets in the window
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# adding buttons and labels in the window
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3,
                                                                row=3,
                                                                sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()