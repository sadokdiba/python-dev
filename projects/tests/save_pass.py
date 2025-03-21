def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as file:
        data_file.write(f"{website} | {email} | {password}")