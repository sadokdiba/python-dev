from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# def print_report(resources, money_received):
#     """
#     Return a formatted string representing the current machine resource status.
#     """
#     return (
#         f"Water: {resources['water']}ml\n"
#         f"Milk: {resources['milk']}ml\n"
#         f"Coffee: {resources['coffee']}g\n"
#         f"Money: ${sum(money_received):.2f}"
#     )

# def main():
#     machine_on = True
#     invalid_inputs_remaining = 3
#     money_received = []
    

#     while machine_on and invalid_inputs_remaining > 0:
#         try:
#             user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
#             if user_choice == 'report':
#                 print(print_report(current_resources, money_received))
#             elif user_choice == 'off':
#                 machine_on = False
#             elif user_choice in MENU:
#                 process_drink(user_choice, MENU, current_resources, money_received)
#             else:
#                 print("Sorry, that's not a valid option. Please try again.")
#                 invalid_inputs_remaining -= 1
#         except KeyboardInterrupt:
#             print("Machine forcefully turned off!")
#             quit()
#     if invalid_inputs_remaining == 0:
#         print("Too many invalid inputs. Please try again later.")


# if __name__ == "__main__":
#     print("Welcome to the Coffee Machine")
#     main()
#     print("Thank you for using the Coffee Machine! Goodbye")

menu = Menu()
moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()

user_choice = input(f"What would you like, {menu.get_items()}?")
if user_choice == 'report':
    moneymachine.report()
else:
    menu.find_drink(user_choice)
    print(f"The {menu.find_drink(user_choice).name} will cost: ${round(menu.find_drink(user_choice).cost, 2)}")
    moneymachine.make_payment(menu.find_drink(user_choice).cost)
    coffeemaker.make_coffee(user_choice)