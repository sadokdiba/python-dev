import time

print("Welcome to Python Pizza Deliveries!")
size = (input("What size pizza do you want? S, M or L: ").strip().upper())
if size == "S":
    price_at_size = 15
elif size == "M":
    price_at_size = 20
elif size == "L":
    price_at_size = 25
else:
    print("incorrect Size of Pizza Entered, Please restart and try again")
    print("GOOD BYE!")
    quit()

price_at_pepperoni = 0
attempts_pepperoni=3
while attempts_pepperoni > 0:
    if size == "S":
        pepperoni_s_pizza = input("Add pepperoni for small pizza? Y or N: ").strip().upper()
        if pepperoni_s_pizza == "Y":
            price_of_s_pepperoni = 2
            price_at_pepperoni = price_of_s_pepperoni
            break
        elif pepperoni_s_pizza == "N":
            price_of_s_pepperoni = price_at_pepperoni = 0
            break
        else:
            attempts_pepperoni -=1
            if attempts_pepperoni > 0:
                print("You have exhausted your attempts, please restart and try again")
                print("GOOD BYE!")
                quit()
            print(f"incorrect Size of Pizza Entered, {attempts_pepperoni} left. Please and try again")
    else:
        if size in ["M","L"]:
            pepperoni_m_l_pizza = input("Add pepperoni for your medium or large pizza? Y or N: ").strip().upper()
            if pepperoni_m_l_pizza == "Y":
                price_of_m_l_pepperoni = 2
                price_at_pepperoni = price_of_m_l_pepperoni
                break
            elif pepperoni_m_l_pizza == "N":
                price_of_m_l_pepperoni = price_at_pepperoni
                break
            else:
                attempts_pepperoni -= 1
                if attempts_pepperoni > 0:
                    print("You have exhausted your attempts, please restart try again")
                    print("GOOD BYE!")
                    quit()
                print(f"incorrect Size of Pizza Entered, {attempts_pepperoni} left. Please try again")

price_of_extra_cheese = 0
attempts_extra_cheese=3
while attempts_extra_cheese > 0:
    extra_cheese = input("Extra cheese for any size pizza? Y or N: ").strip().upper()
    if extra_cheese == "Y":
        price_of_extra_cheese = 1
        break
    elif extra_cheese == "N":
        break
    else:
        attempts_extra_cheese -=1
        if attempts_extra_cheese > 0:
            print("You have exhausted your attempts, please restart and try again")
            print("GOOD BYE!")
            quit()
        print(f"incorrect Size of Pizza Entered, {attempts_extra_cheese} left. Please try again")

final_bill =  price_at_size + price_at_pepperoni + price_of_extra_cheese
print("Calculating...")
time.sleep(3) #pretending to calculate for 3seconds :)
print(f"Your final bill is ${final_bill}. Thank you for ordering!")
