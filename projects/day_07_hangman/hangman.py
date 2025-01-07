import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

game_over = False
correct_letters = []
lives = 6

print(f"{logo}\n\n") # prints the hangman logo
print(f"The word to find has {word_length} letters as such {placeholder} <--- Hidden here")

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    try:
        guess = input("Guess a letter: \n\n").lower()
    except KeyboardInterrupt:
        print("You have exited the game")
        quit()
    except ValueError as e:
        print(f"An error occured: {e}")
        quit()

    if guess in correct_letters:
        print(f"You've already guessed the letter \"{guess}\" ")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display+=guess
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed \"{guess}\", thats not in the word. You loose a life!")
        if lives == 0:
            game_over = True

            print(f"***************************The word was \"{chosen_word}\" - YOU LOOSE*****************************")

    print(display)

    if "_" not in display:
        game_over = True
        print("***************************You win!!!!*****************************")

    print(stages[lives])
