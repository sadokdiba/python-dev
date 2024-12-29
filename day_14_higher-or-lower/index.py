import art
from game_data import data
from random import randint

LENGTH_OF_DATA = len(data)-1
CLEAR_SCREEN = "\n" * 30
INVALID_INPUT_MESSAGE = "Invalid choice. Please type 'A' or 'B'."
GAME_OVER_MESSAGE = "Too many invalid attempts. Restart the game to try again."
CONTINUE_MESSAGE = "Not quite! They each have equal followers."

print(art.logo)

def clear_screen():
    print(CLEAR_SCREEN)

def determine_answer(score, user_choice, choice_a, choice_b, first_random_index, second_random_index):
    """Print the comparison between two options."""
    is_true = False
    if user_choice == 'A' and choice_a > choice_b or user_choice == 'B' and choice_b > choice_a:
        winner, loser = (first_random_index, second_random_index) if user_choice == 'A' else (second_random_index, first_random_index)
        clear_screen()
        print(f"That's right! {data[winner]['name']} has {data[winner]['follower_count']} followers. Which is greater than {data[loser]['name']}'s {data[loser]['follower_count']} followers\nYour current score is {score + 1}\n")
        score += 1
        is_true = True
    elif user_choice == 'A' and choice_a < choice_b or user_choice == 'B' and choice_b < choice_a:
        winner, loser = (second_random_index, first_random_index) if user_choice == 'A' else (first_random_index, second_random_index)
        print(f"That's wrong! {data[loser]['name']} has {data[loser]['follower_count']} followers. Which is smaller than {data[winner]['name']}'s {data[winner]['follower_count']} followers\n")
    else:
        clear_screen()
        print(f"{CONTINUE_MESSAGE} - {data[first_random_index]['follower_count']} and {data[second_random_index]['follower_count']}\nYour current score is still {score}\n - You can continue")
        is_true = True

    return is_true, score

def capture_input(score, choice_a, choice_b, first_rand_ind, second_rand_ind):
    """Capture the user input and return the result."""
    try:
        attempts = 3
        while attempts > 0:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
            if user_choice in ('A', 'B'):
                return determine_answer(score, user_choice, choice_a, choice_b, first_rand_ind, second_rand_ind)
            if attempts == 1:
                break
            else:
                attempts -= 1
                print(f"{INVALID_INPUT_MESSAGE} {attempts} attempt(s) left")
                
        print(GAME_OVER_MESSAGE)
        quit()
    except KeyboardInterrupt:
        print("program ended")
        quit()

def main():
    '''Main game loop'''
    score = 0
    is_true = True
    while is_true:

        first_random_index = randint(0, LENGTH_OF_DATA)
        second_random_index = randint(0, LENGTH_OF_DATA)

        print(f"Compare A: {data[first_random_index]['name']}, {data[first_random_index]['description']}, from {data[first_random_index]['country']}\n")
        print(art.vs)
        print(f"Compare B: {data[second_random_index]['name']}, {data[second_random_index]['description']}, from {data[second_random_index]['country']}\n")

        choice_a = data[first_random_index]['follower_count']
        choice_b = data[second_random_index]['follower_count']

        is_true, score = capture_input(score, choice_a, choice_b, first_random_index, second_random_index)

    print(f"Your final score is {score}")

if __name__ == "__main__":
    main()