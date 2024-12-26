from art import logo
from art import auction_rules

prompt_name = "What is your name:\n"
prompt_bid = "What is your bid price: $"
prompt_more_bidders = "Are there any other bidders? (y/n):\n"
max_attempts = 3
max_bidders = 5
max_name_length = 32
min_bid_amount = 100
max_bid_amount = 1000000

def clear_screen():
    print("\n" * 20)

def get_bid():
    attempts_left = max_attempts
    while attempts_left > 0:
        try:
            bidder_name = input(prompt_name).strip()
            if not bidder_name:  # Check if name is empty
                attempts_left -= 1
                print(f"Name cannot be empty. {attempts_left} attempts remaining.")
                continue

            if len(bidder_name) > max_name_length:
                attempts_left -= 1
                print(f"Name entered too long. Enter {max_name_length} chars or less, spaces included. {attempts_left} attempts remaining.")
                continue

            bid_amount = float(input(prompt_bid).strip())
            
            if bid_amount < min_bid_amount:
                attempts_left -= 1
                print(f"Minimun bid amount ${min_bid_amount}. {attempts_left} attempts remaining.\n\nStart Again!\n\n")
                continue

            if bid_amount > max_bid_amount:
                attempts_left -= 1
                print(f"Bid amount must not exceed $1,000,000. {attempts_left} attempts remaining.\n\nStart Again!\n\n")
                continue

            return bidder_name, bid_amount  # Return valid name and bid amount
        
        except KeyboardInterrupt:
            print("You have exited the program.")
            quit()
        except ValueError:
            attempts_left -= 1
            print(f"Bid price must be a number. {attempts_left} attempts remaining.")
    
        print("Too many invalid attempts. Exiting.")
        quit()
            
def determine_winner(bids):
    winner_key = max(bids, key=bids.get)
    winner_value = bids[winner_key]
    return winner_key, winner_value

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
    print("Too many invalid attempts. Exiting.")
    quit()

def main():
    print(logo)
    print(auction_rules)

    bidders_data = {} # where all new data will be stored
    is_bidding_active = True

    while is_bidding_active:
        bidder_name, bid_amount = get_bid()
        bidders_data[bidder_name] = bid_amount

        if len(bidders_data) >= max_bidders:
            print("Max bidders reached!")
            break

        is_bidding_active = prompt_for_more_bidders()

        if is_bidding_active:
            clear_screen()

    winner_name, winner_bid = determine_winner(bidders_data)

    print(f"All bidders' data: {bidders_data}")
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")

if __name__ == "__main__":
    main()