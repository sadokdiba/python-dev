import art
from game_data import data
import random

CLEAR_SCREEN = "\n" * 50
INVALID_INPUT_MESSAGE = "Invalid choice. Please type 'A' or 'B'."
GAME_OVER_MESSAGE = "Too many invalid attempts. Restart the game to try again."
CONTINUE_MESSAGE = "Not quite! They each have equal followers."
print(art.logo)

def clear_screen():
    print(CLEAR_SCREEN)

def format_data(account):
    """Format the account data into printable format."""
    acc_name = account["name"]
    acc_des = account["description"]
    acc_cntry = account["country"]
    return f"{acc_name}, a {acc_des}, from {acc_cntry}"

def print_comparison(choice_a, choice_b):
    """Print the comparison between two options."""
    print(f"Compare A: {format_data(choice_a)}.\n")
    print(art.vs)
    print(f"Compare B: {format_data(choice_b)}.\n")

def determine_answer(score, user_choice, choice_a, choice_b):
    """Print the comparison between two options."""
    is_true = False
    if user_choice == 'A' and choice_a['follower_count'] > choice_b['follower_count'] or user_choice == 'B' and choice_b['follower_count'] > choice_a['follower_count']:
        winner, loser = (choice_a, choice_b) if user_choice == 'A' else (choice_b, choice_a)
        clear_screen()
        print(f"That's right! {winner['name']} has {winner['follower_count']} followers. Which is greater than {loser['name']}'s {loser['follower_count']} followers\nYour current score is {score + 1}\n")
        score += 1
        is_true = True
    elif user_choice == 'A' and choice_a['follower_count'] < choice_b['follower_count'] or user_choice == 'B' and choice_b['follower_count'] < choice_a['follower_count']:
        winner, loser = (choice_b, choice_a) if user_choice == 'A' else (choice_a, choice_b)
        print(f"That's wrong! {loser['name']} has {loser['follower_count']} followers. Which is smaller than {winner['name']}'s {winner['follower_count']} followers\n")
    else:
        clear_screen()
        print(f"{CONTINUE_MESSAGE} - {choice_a['follower_count']} and {choice_b['follower_count']}\nYour current score is still {score}\n - You can continue")
        is_true = True
    return is_true, score

def capture_input(score, choice_a, choice_b):
    """Capture the user input and return the result."""
    try:
        attempts = 3
        while attempts > 0:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
            if user_choice in ('A', 'B'):
                return determine_answer(score, user_choice, choice_a, choice_b)
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
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    while choice_a == choice_b:
        choice_b = random.choice(data)
    previous_a, previous_b = choice_a, choice_b
    print_comparison(choice_a, choice_b)
    while is_true:
        is_true, score = capture_input(score, choice_a, choice_b)
        if not is_true:
            break
        if choice_a['follower_count'] > choice_b['follower_count']:
            choice_a, choice_b = previous_a, random.choice(data)
        else:       
            choice_a, choice_b = previous_b, random.choice(data)
        while choice_a == choice_b:
            choice_b = random.choice(data)
        previous_a, previous_b = choice_a, choice_b
        print_comparison(choice_a, choice_b)
    print(f"Your final score is {score}.")

if __name__ == "__main__":
    main()
