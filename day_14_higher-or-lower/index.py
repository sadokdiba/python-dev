import art
from game_data import data
from random import randint

LENGTH = len(data)-1
print(art.logo)

def clear_screen():
    print("\n" *30)

def determine_answer(score_update, response, choice_a, choice_b, first_random_index, second_random_index):

    if response == 'A' and choice_a > choice_b:
        is_true_update = True
        score_update += 1
        clear_screen()
        print(f"That's right! {data[first_random_index]['name']} has {data[first_random_index]['follower_count']} followers greater than {data[second_random_index]['name']}'s {data[second_random_index]['follower_count']} followers\nYour current score is {score_update}\n")
        return is_true_update, score_update

    elif response == 'A' and choice_a < choice_b:
        print(f"That's wrong! {data[first_random_index]['name']} has {data[first_random_index]['follower_count']} followers less than {data[second_random_index]['name']}'s {data[second_random_index]['follower_count']} followers\n")
        is_true_update = False
        return is_true_update, score_update

    elif response == 'B' and choice_a < choice_b:
        is_true_update = True
        score_update += 1
        clear_screen()
        print(f"That's right! {data[second_random_index]['name']} has {data[second_random_index]['follower_count']} followers greater than {data[first_random_index]['name']}'s {data[first_random_index]['follower_count']} followers\nYour current score is {score_update}\n")
        return is_true_update, score_update

    elif response == 'B' and choice_a > choice_b:
        print(f"That's wrong! {data[second_random_index]['name']} has {data[second_random_index]['follower_count']} followers less than {data[first_random_index]['name']}'s {data[first_random_index]['follower_count']} followers\n")
        is_true_update = False
        return is_true_update, score_update
    else:
        clear_screen()
        print(f"Not quite! They each have equal followers - {data[first_random_index]['follower_count']} and {data[second_random_index]['follower_count']}\nYour current score is still {score_update}\n - You can continue")
        is_true_update = True
        return is_true_update, score_update

def capture_input(score_capture, choice_a_capture, choice_b_capture, first_rand_ind, second_rand_ind):
    try:
        for _ in range(3):
            resp = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
            if resp in ('A', 'B'):
                is_true_capture, score_capture = determine_answer(score_capture, resp, choice_a_capture, choice_b_capture, first_rand_ind, second_rand_ind)
                return is_true_capture, score_capture
            else:
                print("Invalid choice. Please type 'easy' or 'hard'.\n")
        print("Too many invalid attempts. Restart the game to try again.")
        quit()
    except KeyboardInterrupt:
        print("program ended")

def main():
    score = 0
    is_true = True
    while is_true:

        first_random_index = randint(0, LENGTH)
        second_random_index = randint(0, LENGTH)

        print(f"Compare A: {data[first_random_index]['name']}, {data[first_random_index]['description']}, from {data[first_random_index]['country']}\n")
        print(art.vs)
        print(f"Compare B: {data[second_random_index]['name']}, {data[second_random_index]['description']}, from {data[second_random_index]['country']}\n")

        choice_a = data[first_random_index]['follower_count']
        choice_b = data[second_random_index]['follower_count']

        is_true, score = capture_input(score, choice_a, choice_b, first_random_index, second_random_index)

    print(f"Your final score is {score}")

if __name__ == "__main__":
    main()