from tkinter import *
import pyperclip
import random
import csv
import os
from tkinter import messagebox
from password_utils import passwordValidator

pwd_validator = passwordValidator()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = []
    length = length_slider.get()

    letter_count = int(length * 0.7)  # 70% letters
    number_count = int(length * 0.2)  # 20% numbers
    symbol_count = length - letter_count - number_count  # remaining for symbols
    
    for _ in range(letter_count):
        password.append(random.choice(pwd_validator.letters))
    
    for _ in range(number_count):
        password.append(random.choice(pwd_validator.numbers))
    
    for _ in range(symbol_count):
        password.append(random.choice(pwd_validator.symbols))
    
    # Shuffle to make it random
    random.shuffle(password)
    password = ''.join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get()

    # Validate inputs
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please fill all fields!")
        return

    if not pwd_validator.validate_website(website):
        messagebox.showwarning(title="Invalid Website", message="Please enter a valid website address!\nExample: google.com")
        return

    if not pwd_validator.validate_email(email):
        messagebox.showwarning(title="Invalid Email", message="Please enter a valid email address!\nExample: example@email.com")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}" f"\nPassword: {password}\nIs it ok to save?")
    
#     if is_ok:
#         with open("passwords.txt", "a") as file:
#             file.write(f"{website} | {email} | {password}\n")
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
#             website_entry.focus()
    
    if is_ok:
        fieldnames = ['website', 'email', 'password']
        file_exists = os.path.isfile('passwords.csv')
        
        with open('passwords.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header only if file is new
            if not file_exists:
                writer.writeheader()
            
            # Write the new row
            writer.writerow({
                'website': website,
                'email': email,
                'password': password
            })
            
        # Clear entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sadokdiba@gmail.com")
email_entry.focus()

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

length_label = Label(text="Length:")
length_label.grid(column=0, row=4)

length_slider = Scale(window, from_=8, to=32, orient=HORIZONTAL, length=200)
length_slider.set(16)  # Default value
length_slider.grid(column=1, row=4, columnspan=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()

