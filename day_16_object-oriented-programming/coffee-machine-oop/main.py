from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def print_report():
    coffeemaker.report()
    moneymachine.report()

menu = Menu()
moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()

def main():
    machine_on = True
    invalid_inputs_remaining = 3
    while machine_on and invalid_inputs_remaining > 0:
        try:
            user_choice = input(f"What would you like, {menu.get_items()}?")

            if user_choice == 'report':
                print_report()
            elif user_choice == 'off':
                machine_on = False
            else:

                cost = menu.find_drink(user_choice).cost
                drink = menu.find_drink(user_choice)

                if coffeemaker.is_resource_sufficient(drink):
                
                    menu.find_drink(user_choice)
                    print(f"The {menu.find_drink(user_choice).name} will cost: ${round(menu.find_drink(user_choice).cost, 2)}")
                    
                    moneymachine.make_payment(cost)
                    coffeemaker.make_coffee(drink)
                
        except AttributeError as e:
            print(f"you've enterred an invalid input ({e})")
            invalid_inputs_remaining -= 1
        except KeyboardInterrupt:
            print("Machine forcefully turned off!")
            machine_on = False

if __name__ == "__main__":
    print("Welcome to the Coffee Machine")
    main()
    print("Thank you for using the Coffee Machine! Goodbye")
