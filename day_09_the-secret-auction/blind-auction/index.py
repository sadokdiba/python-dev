from art import logo
from art import auction_rules

prompt_name = "What is your name?:\n"
prompt_bid = "What is your bid price?: $"
prompt_more_bidders = "Are there any other bidders? (y/n):\n"
max_attempts = 5
max_bidders = 5
max_name_length = 6
min_bid_amount = 100
max_bid_amount = 1000000

def clear_screen():
    print("\n" * 50)

def get_bidder_name(names):

    name_attempts_left = max_attempts
    while name_attempts_left > 0:
        try:
            bidder_name = input(prompt_name).strip()

            # Build a new dict of bidders_data called data_lower with keys in lower while keeping value intact:
            data_lower = {k.lower(): v for k, v in names.items()}

            # Find all elements in the list that match keys in lower
            lookup_matches = bidder_name.lower()
            if lookup_matches in data_lower:
                name_attempts_left -= 1
                print("Name is already in the list, enter a different name.")
                continue

            # Check if name is empty
            if not bidder_name:  
                name_attempts_left -= 1
                if name_attempts_left == 0:
                    break
                print(f"Name cannot be empty. {name_attempts_left} attempts remaining.\n")
                continue

            if len(bidder_name) > max_name_length:
                name_attempts_left -= 1
                if name_attempts_left == 0:
                    break
                print(f"Name entered too long. Enter {max_name_length} chars or less (spaces included). "
                      f"{name_attempts_left} attempts remaining.\n")
                continue

            return bidder_name
        
        except KeyboardInterrupt:
            print("You have exited the program.")
            quit()
    print("\nMax attempts reached for NAME!\n"
     "Please read instructions carefully at start and try again.\nExiting.")
    quit()

def get_bid_amount():
    bid_attempts_left = max_attempts
    while bid_attempts_left > 0:
        try:
            bid_amount = float(input(prompt_bid).strip())

            if bid_amount < min_bid_amount:
                bid_attempts_left -= 1
                if bid_attempts_left == 0:
                    print("\nMax attempts reached for BID!\n"
                          "Please read instructions carefully at start and try again.\nExiting.")
                    quit()
                print(f"Minimum bid amount is ${min_bid_amount:,.2f}. {bid_attempts_left:,.2f} attempts remaining.\n")
                continue

            if bid_amount > max_bid_amount:
                bid_attempts_left -= 1
                if bid_attempts_left == 0:
                    print("\nMax attempts reached for BID!\n"
                          "Please read instructions carefully at start and try again.\nExiting.")
                    quit()
                print(f"Bid amount must not exceed ${max_bid_amount}. "
                      f"{bid_attempts_left} attempts remaining.\n\nStart Again!\n")
                continue

            return bid_amount

        except KeyboardInterrupt:
            print("You have exited the program.")
            quit()

        except ValueError:
            bid_attempts_left -= 1
            if bid_attempts_left == 0:
                break
            print(f"Bid price must be a number. {bid_attempts_left} attempts remaining.\n")

    print("\nMax attempts reached!\n"
          "Please read instructions carefully at start and try again.\nExiting.")
    quit()

def determine_winner(bids):
    # winner_key = max(bids, key=bids.get)
    # winner_value = bids[winner_key]
    # return winner_key, winner_value
    winner_key = ""
    highest_bid_amount = 0
    for key in bids:
        value = bids[key]
        if value > highest_bid_amount:
            highest_bid_amount = value
            winner_key = key
    return winner_key, highest_bid_amount

def prompt_for_more_bidders():
    attempts_left = max_attempts
    while attempts_left > 0:
        try:
            response = input(prompt_more_bidders).strip().lower()
            if response in ("y", "n"):
                return response == "y"  # Return True for "y", False for "n" (high level, I know!)
            else:
                attempts_left -= 1
                print(f"Invalid input. Please type 'y' for yes or 'n' for no. {attempts_left} attempts remaining.")
        except KeyboardInterrupt:
                print("You have exited the program.")
                quit()
        except ValueError as e:
            print(f"An error occurred: {e}")
    print("Max attempts reached!\nPlease carefully read instructions at the start and try again.\nExiting.")
    quit()

def main():
    print(logo)
    print(auction_rules)

    bidders_data = {} # final bidders dict

    is_bidding_active = True

    while is_bidding_active:
        try:
            bidder_name = get_bidder_name(names=bidders_data)
            bid_amount = get_bid_amount()
            bidders_data[bidder_name] = bid_amount #storing bidders in the bidders_data dict while bidding active

            if len(bidders_data) >= max_bidders:
                print(f"Max bidders of {max_bidders} reached!")
                break

            is_bidding_active = prompt_for_more_bidders()

            if is_bidding_active:
                clear_screen()
        except ValueError as e:
            print(f"An error occured: {e}")

    winner_name, winner_bid = determine_winner(bidders_data)
    print("\nThats the end of the auction!")
    print(f"Bidders' data:")
    for key in bidders_data:
        print(f"{key}------>${bidders_data[key]:,.2f}")
        
    print(f"\nThe winner is {winner_name} with a bid of ${winner_bid:,.2f}\nCongratulations!\n")

if __name__ == "__main__":
    main()