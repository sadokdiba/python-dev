import random
import art

def play_game(num_to_guess, range_set, attempts):

    """Handles the game logic for both difficulty levels."""

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.\n")
        try:
            num_guessed_by_user = int(input("Make a guess: \n"))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        except KeyboardInterrupt:
            print("\nYou have ended the program. Goodbye!")
            quit()

        if num_guessed_by_user == num_to_guess:
            print("\nYou got it! Well done!")
            return
        elif 1 <= num_guessed_by_user <= range_set:
            if num_guessed_by_user < num_to_guess:
                print("Too low.\nGuess again.\n")
            else:
                print("Too high.\nGuess again.\n")
            attempts -= 1
        else:
            print(f"Please only enter numbers between 1 and {range_set}.\n")

    print(f"You've run out of guesses. The number to guess was {num_to_guess}.\n")

def main():

    """Main function to run the number guessing game."""
    
    range_of_game = 100  # Upper limit for the range
    num_to_guess = random.randint(1, range_of_game)  # Includes both 1 and 100

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {range_of_game}.")

    try:
        for _ in range(3):  # Allow 3 attempts to choose the difficulty.
            level_chosen_by_user = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
            if level_chosen_by_user == "easy":
                play_game(num_to_guess, range_of_game, attempts=10)
                return
            elif level_chosen_by_user == "hard":
                play_game(num_to_guess, range_of_game, attempts=5)
                return
            else:
                print("Invalid choice. Please type 'easy' or 'hard'.\n")
    except KeyboardInterrupt:
        print("\nYou have ended the program. Goodbye!")
        quit()

    print("Too many invalid attempts. Restart the game to try again.")

if __name__ == "__main__":
    main()