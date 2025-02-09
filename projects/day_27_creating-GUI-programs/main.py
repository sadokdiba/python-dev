from tkinter import *

window = Tk()
window.title("Python program")
window.minsize(width=600, height=500)

#Labels
label = Label()
label.config(text="Click the below button to perform some action.", font=("Arial", 24, "bold"))
label.pack()

#Buttons
def action():
    pass

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

# #Text
# text = Text(height=5, width=5)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

window.mainloop()