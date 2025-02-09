from tkinter import *

# Window Configuration
root = Tk()
root.title("Interactive Widget Demo")
root.minsize(width=600, height=600)
root.configure(bg="#f0f0f0")

# Custom Label
greeting = Label(
    text="Welcome to Widget Demo",
    font=("Helvetica", 16, "bold"),
    bg="#f0f0f0",
    fg="#333333"
) 
greeting.pack(pady=10)

# Custom Button
def button_action():
    greeting.config(text="Thanks for clicking!")

demo_button = Button(
    text="Press Here",
    command=button_action,
    bg="#4CAF50",
    fg="brown",
    padx=10
)
demo_button.pack()

# Input Field
user_input = Entry(
    width=35,
    justify="center"
)
user_input.insert(0, "Type something here...")
user_input.pack(pady=10)

# Multi-line Text Area
notes_area = Text(
    height=4,
    width=35,
    font=("Arial", 10)
)
notes_area.insert("1.0", "Write your notes here...\n")
notes_area.pack(pady=10)

# Number Selector
def value_changed():
    greeting.config(text=f"Selected: {number_selector.get()}")

number_selector = Spinbox(
    from_=1,
    to=20,
    width=10,
    command=value_changed
)
number_selector.pack()

# Slider Control
def slider_moved(val):
    notes_area.insert(END, f"Slider value: {val}\n")

intensity = Scale(
    from_=0,
    to=100,
    orient="horizontal",
    command=slider_moved
)
intensity.pack(pady=10)

# Toggle Switch
def toggle_changed():
    status = "ON" if toggle_var.get() else "OFF"
    greeting.config(text=f"Toggle is {status}")

toggle_var = IntVar()
toggle = Checkbutton(
    root,
    text="Enable Feature",
    variable=toggle_var,
    command=toggle_changed
)
toggle.pack()

# Option Selector
def option_selected():
    greeting.config(text=f"Option {option_var.get()} selected")

option_var = IntVar()
option1 = Radiobutton(
    root,
    text="Choice A",
    value=1,
    variable=option_var,
    command=option_selected
)
option2 = Radiobutton(
    root,
    text="Choice B",
    value=2,
    variable=option_var,
    command=option_selected
)
option1.pack()
option2.pack()

# Selection List
def list_selected(event):
    selection = items_list.get(items_list.curselection())
    greeting.config(text=f"Selected: {selection}")

items_list = Listbox(
    root,
    height=4,
    selectmode="single"
)
items = ["Python", "JavaScript", "Java", "C++"]
for idx, item in enumerate(items):
    items_list.insert(idx, item)
items_list.bind("<<ListboxSelect>>", list_selected)
items_list.pack(pady=10)

root.mainloop()