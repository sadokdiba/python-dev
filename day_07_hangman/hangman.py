import random
from hangman_words import word_list
from hangman_art import stages, logo

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

game_over = False
correct_letters = []
lives = 6

print(logo) # prints the hangman logo

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: \n\n").lower()

    if guess in correct_letters:
        print(f"You've already guessed the letter \"{guess}\" ")

    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed \"{guess}\", thats not in the word. You loose a life!")
        if lives == 0:
            game_over = True

            print("***************************YOU LOOSE*****************************")

    print(display)

    if "_" not in display:
        game_over = True
        print("***************************You win!!!!*****************************")

    print(stages[lives])
