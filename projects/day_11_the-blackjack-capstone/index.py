import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def brain_of_game(us_cards, comp_cards, igo, comp_score, us_score):

    while not igo:
        try:
            us_score = calculate_score(us_cards)
            comp_score = calculate_score(comp_cards)
            print(f"Your cards: {us_cards}, current score: {us_score}")
            print(f"Computer's first card: {comp_cards[0]}")

            if us_score == 0 or comp_score == 0 or us_score > 21:
                igo = True
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal == "y":
                    us_cards.append(deal_card())
                else:
                    igo = True

        except KeyboardInterrupt:
            print("Program ended with Keyborad Shortcut")
            quit()
        except ValueError as e:
            print(f"An error occurred: {e}")
            quit()

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {us_cards}, final score: {us_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(us_score, comp_score))

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    brain_of_game(comp_score=computer_score, us_score=user_score, igo=is_game_over , us_cards=user_cards, comp_cards=computer_cards)

    continue_playing = True
    while continue_playing:
        
        try:
            continue_playing_response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
            if continue_playing_response == "y":
                print("\n" * 20)
                play_game()
            else:
                continue_playing = False

        except KeyboardInterrupt:
            print("Program ended with Keyborad Shortcut")
            quit()
        except ValueError as e:
            print(f"An error occurred: {e}")
            quit()

    print("Thanks for playing - Good Bye")
    quit()

if __name__ == "__main__":
    play_game()