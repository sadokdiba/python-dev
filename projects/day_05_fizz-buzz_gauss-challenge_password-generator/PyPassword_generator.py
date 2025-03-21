import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for _ in range(0, nr_letters):
    password_list.append(random.choice(letters))
for _ in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

final_password = ""
for char in password_list:
    final_password += char
print(f"Your password with for loop is: {final_password}")

final_password = "".join(password_list)
print(f"Your password with join is: {final_password}")

# You can only shuffle a list and the shuffle needs to happen without being assigned to a variable

str_password = list(final_password)
random.shuffle(str_password)
final_restring = ""

for v in (str_password):
    final_restring+=v

print(f"You final password shuffled :{final_restring}")



