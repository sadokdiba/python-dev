import time

def peperoni_check(size, price_at_size):
    price_at_pepperoni = 0
    attempts_pepperoni = 3
    while attempts_pepperoni > 0:
        if size == "S":
            pepperoni_s_pizza = input("Add pepperoni for small pizza? Y or N: ").strip().upper()
            if pepperoni_s_pizza == "Y":
                price_at_pepperoni = 2
                break
            elif pepperoni_s_pizza == "N":
                break
        elif size in ["M", "L"]:
            while attempts_pepperoni > 0:
                pepperoni_m_l_pizza = input("Add pepperoni for your medium or large pizza? Y or N: ").strip().upper()
                if pepperoni_m_l_pizza == "Y":
                    price_at_pepperoni = 3
                    break
                elif pepperoni_m_l_pizza == "N":
                    break
                else:
                    attempts_pepperoni -= 1
                    if attempts_pepperoni == 0:
                        print("You have exhausted your attempts. Please restart and try again.")
                        quit()
                    print(f"Incorrect input. {attempts_pepperoni} attempts left.")
            break
        else:
            attempts_pepperoni -= 1
            if attempts_pepperoni == 0:
                print("You have exhausted your attempts. Please restart and try again.")
                quit()
            print(f"Incorrect input. {attempts_pepperoni} attempts left.")
    return price_at_size, price_at_pepperoni

def cheese_check(price_at_size, price_at_pepperoni):
    price_of_extra_cheese = 0
    attempts_extra_cheese = 3
    while attempts_extra_cheese > 0:
        extra_cheese = input("Extra cheese for any size pizza? Y or N: ").strip().upper()
        if extra_cheese == "Y":
            price_of_extra_cheese = 1
            break
        elif extra_cheese == "N":
            break
        else:
            attempts_extra_cheese -= 1
            if attempts_extra_cheese == 0:
                print("You have exhausted your attempts. Please restart and try again.")
                quit()
            print(f"Incorrect input. {attempts_extra_cheese} attempts left.")
    final_bill = price_at_size + price_at_pepperoni + price_of_extra_cheese
    return final_bill

def display_final_bill(final_bill):
    print("Calculating...")
    time.sleep(3)  # Pretend to calculate for 3 seconds :)
    print(f"Your final bill is ${final_bill}. Thank you for ordering!")

def main():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L: ").strip().upper()
    if size == "S":
        price_at_size = 15
    elif size == "M":
        price_at_size = 20
    elif size == "L":
        price_at_size = 25
    else:
        print("Incorrect size of pizza entered. Please restart and try again.")
        print("GOODBYE!")
        quit()

    price_at_size, price_at_pepperoni = peperoni_check(size, price_at_size) #calls the function peperoni_check and passing size and price_at_size arguments / receive the price_at_pepperoni updated value back from peperoni_check
    final_bill = cheese_check(price_at_size, price_at_pepperoni) #calls the function cheese_check and passing price_at_size and price_at_pepperoni / receive back the final_bill value from the cheese_check function
    display_final_bill(final_bill) #calls the function display bill and passes the argument final_bill

if __name__ == "__main__":
    main()
