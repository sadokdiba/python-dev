from tkinter import *

window = Tk()
window.title("GUI PROGRAM")
window.minsize(width=500, height=300)

my_label = Label(text="Testing Label", font=("Arial", 16, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=f"{new_text}")


button = Button(text="Click Me", font=("Arial", 24), command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
# print(input.get())







window.mainloop()