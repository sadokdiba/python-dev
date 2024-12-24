alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):

    shifted_text = ""

    for letter in text:
        if letter in alphabet:
            original_index_letter = alphabet.index(letter)
            new_index_letter = original_index_letter+shift
            new_index_letter %= len(alphabet) #ensures that by whatever amount the user wants to shift, it stays within the length of the alphabet list
            new_letter_after_shift = alphabet[new_index_letter]
            shifted_text += new_letter_after_shift
        else:
            shifted_text += letter
    print(f"Here is the encoded result {shifted_text}")

encrypt(text,shift)