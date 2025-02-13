from menu import MENU, resources

def print_report(resources, money_received):
    """
    Return a formatted string representing the current machine resource status.
    """
    return (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${sum(money_received):.2f}"
    )

def capture_money():
    """
    Prompt the user for coin inputs and return the total monetary value.
    Retries up to 3 times for invalid input.
    """
    invalid_inputs_remaining = 3
    while invalid_inputs_remaining > 0:
        try:
            quarters = int(input("How many quarters? ($0.25 each) "))
            dimes = int(input("How many dimes? ($0.10 each) "))
            nickels = int(input("How many nickels? ($0.05 each) "))
            pennies = int(input("How many pennies? ($0.01 each) "))
            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            return total
        except ValueError:
            print("Sorry, that's not a valid input. Please try again.")
            invalid_inputs_remaining -= 1

    print("Too many invalid inputs. Please try again later.")
    quit()

def check_resources(drink_name, menu, current_resources):
    """
    Check if there are enough resources to make the selected drink.
    Return True if sufficient, False otherwise.
    """
    ingredients = menu[drink_name]['ingredients']
    for ingredient, required_amount in ingredients.items():
        if current_resources[ingredient] < required_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_drink(drink_name, menu, resources, money_received):
    """
    Handle the entire drink process:
      1. Check resources
      2. Capture payment
      3. Check payment
      4. Deduct resources
      5. Update money received
    """
    cost = menu[drink_name]['cost']

    if not check_resources(drink_name, menu, resources):
        return
    print(f"The {drink_name} will cost: ${cost:.2f}")

    total_received = capture_money()
    
    if total_received < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return
    else:
        change = total_received - cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")

        for ingredient, required_amount in menu[drink_name]['ingredients'].items():
            resources[ingredient] -= required_amount

        money_received.append(cost)
        print(f"Here is your {drink_name} ☕️. Enjoy!")

def refill_resources(resources):
    """
    Refill the machine's resources.
    """
    resources['water'] += int(input("How much water to add? (ml): "))
    resources['milk'] += int(input("How much milk to add? (ml): "))
    resources['coffee'] += int(input("How much coffee to add? (g): "))
    print("Resources refilled successfully!")

def main():
    machine_on = True
    invalid_inputs_remaining = 3
    current_resources = resources.copy()
    money_received = []

    while machine_on and invalid_inputs_remaining > 0:
        try:
            user_choice = input("What would you like? (espresso/latte/cappuccino/report/refill/off): ").strip().lower()
            if user_choice == 'report':
                print(print_report(current_resources, money_received))
            elif user_choice == 'refill':
                refill_resources(current_resources)
            elif user_choice == 'off':
                machine_on = False
            elif user_choice in MENU:
                process_drink(user_choice, MENU, current_resources, money_received)
            else:
                print("Sorry, that's not a valid option. Please try again.")
                invalid_inputs_remaining -= 1
        except KeyboardInterrupt:
            print("Machine forcefully turned off!")
            quit()
    if invalid_inputs_remaining == 0:
        print("Too many invalid inputs. Please try again later.")

if __name__ == "__main__":
    print("Welcome to the Coffee Machine")
    main()
    print("Thank you for using the Coffee Machine! Goodbye")