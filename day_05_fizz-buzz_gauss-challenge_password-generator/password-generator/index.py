import random
from chars import letters 
from chars import numbers 
from chars import symbols

print("Welcome to the PyPassword Generator!")
password_length = int(input("How long would you like your password to be?\n"))

char_type = ['letter', 'number', 'symbols']

password_list = []

for char in range(password_length):
    random_char_type = random.choice(char_type)
    if random_char_type == 'letter':
        password_list.append(random.choice(letters))
    elif random_char_type == 'number':
        password_list.append(random.choice(numbers))
    else:
        password_list.append(random.choice(symbols))

print(f"Unshuffled password list {password_list}")
random.shuffle(password_list)
print(f"Shuffled password list {password_list}")

final_password = ""   
for char in password_list:
    final_password+=char

print(f"Final password with \"for loop\": {final_password} ")

final_password = ''.join(password_list)
print(f"Final password with \"join fn\": {final_password} ")