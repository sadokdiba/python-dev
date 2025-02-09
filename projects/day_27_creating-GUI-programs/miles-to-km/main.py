from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=20, pady=20)

miles_entry = Entry(width=10, justify="left")
miles_entry.insert(0, "0")
miles_entry.grid(column=1, row=0, padx=10, pady=10)

miles=Label(text="Miles")
miles.grid(column=2, row=0, padx=10, pady=10)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1, padx=10, pady=10)

result = Label(text="0")
result.grid(column=1, row=1, padx=10, pady=10)

kilometers = Label(text="Km")
kilometers.grid(column=2, row=1, padx=10, pady=10)

def calculate():
    miles = float(miles_entry.get())
    km = miles * 1.60934
    result.config(text=f"{km: .2f}")

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2, padx=10, pady=10)



window.mainloop()