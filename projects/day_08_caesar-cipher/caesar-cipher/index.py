from artalpha import logo
from artalpha import alphabet

print(logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

def get_valid_direction():
    attempts = 3
    while attempts > 0:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ('encode', 'decode'):
            return direction
        else:
            attempts -= 1
            print(f"Invalid input! You have {attempts} attempts left.")

    print("Too many invalid attempts. Goodbye.")
    quit()

def get_valid_message():
    attempts = 3
    while attempts > 0:
        message = input("Type your message (must not contain numbers):\n").strip().lower()
        if message.replace(" ", "").isalpha() and len(message) <= 16: # "replace(" ", "")"" removes spaces before performing isalpha check
            return message
        else:
            attempts -= 1
            print(
                f"Invalid input!\nMessage must be a string without numbers and no more than 16 characters including spaces.\nYou have {attempts} attempts left.")

    print("Too many invalid attempts. Goodbye.")
    quit()

def get_valid_shift():
    attempts = 3
    while attempts > 0:
        try:
            shift = int(input("Type the shift number:\n").strip())
            return shift
        except ValueError:
            attempts -= 1
            print(f"Invalid number! You have {attempts} attempts left.")

    print("Too many invalid attempts. Goodbye.")
    quit()

def main():
    try:
        should_continue = True
        while should_continue:
            
            direction = get_valid_direction()
            text = get_valid_message()
            shift = get_valid_shift()

            caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

            restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").strip().lower()
            if restart == "no":
                should_continue = False
                print("Goodbye")
            elif restart == "yes":
                continue
            else:
                should_continue = False
                print("Invalid selection. Goodbye")
    except KeyboardInterrupt:
        print("You have exited the program: Good Bye")
    except ValueError as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    main()
