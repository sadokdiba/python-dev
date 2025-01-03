from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def print_report(moneymachine, coffeemaker):
    coffeemaker.report()
    moneymachine.report()

def handle_user_input(user_choice, menu, moneymachine, coffeemaker):

    if user_choice == 'report':
        print_report(moneymachine, coffeemaker)
    elif user_choice == 'off':
        return False
    else:
        drink = menu.find_drink(user_choice)
        cost = drink.cost

        if coffeemaker.is_resource_sufficient(drink):
            print(f"The {drink.name} will cost: ${round(cost, 2)}")
            
            if moneymachine.make_payment(cost):
                coffeemaker.make_coffee(drink)

        return True
    
def main():
    menu = Menu()
    moneymachine = MoneyMachine()
    coffeemaker = CoffeeMaker()

    machine_on = True
    invalid_inputs_remaining = 3

    while machine_on and invalid_inputs_remaining > 0:
        try:
            user_choice = input(f"What would you like, {menu.get_items()}?").strip().lower()

            machine_on = handle_user_input(user_choice, menu, moneymachine, coffeemaker)
                
        except AttributeError as e:
            print(f"Invalid input: {e}")
            invalid_inputs_remaining -= 1
        except KeyboardInterrupt:
            print("Machine forcefully turned off!")
            machine_on = False

if __name__ == "__main__":
    print("Welcome to the Coffee Machine")
    main()
    print("Thank you for using the Coffee Machine! Goodbye")