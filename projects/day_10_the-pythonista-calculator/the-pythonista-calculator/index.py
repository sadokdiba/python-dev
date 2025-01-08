import art

print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division
}
def clear_screen():
    print("\n" * 50)

def print_operations():
    for k in operations_dict:
        print(k)

def operating_cell(n1,n2,op):
    if op == "+":
        result = operations_dict["+"](n1,n2)
        return result
    elif op == "-":
        result = operations_dict["-"](n1,n2)
        return result
    elif op == "*":
        result = operations_dict["*"](n1,n2)
        return result
    elif op == "/":
        result = operations_dict["/"](n1, n2)
        return result
    else:
        return ValueError
    
def pick_operation():
    attempts = 3
    while attempts > 0:
        print_operations()
        pick_an_operation = input("Pick an operation: ")
        if pick_an_operation not in operations_dict:
            print("Invalid operation selected")
            attempts -= 1
        else:
            return pick_an_operation
    print("too many invalid attempts")
    quit()

def next_number():
    second_number = float(input("Whats the next number?: "))
    return second_number

def continue_calculating(result):
    is_continue = True
    while is_continue:
        continue_value = input(f"Type 'y' to continue calculating with {result}, Type 'n' to start a new calculation or type any key to exit ")
        if continue_value == 'y':
            clear_screen()
            next_operation = pick_operation()
            next_value = next_number()
            new_result = operating_cell(n1=result,n2=next_value,op=next_operation)
            result = new_result
        elif continue_value == 'n':
            clear_screen()
            is_continue = False
        else:
            return False
    return True

def main():
    is_calculating = True
    while is_calculating:
        try:
            first_number = float(input("What's the first number?: "))
            operation = pick_operation()
            second_number = next_number()
            final_answer = operating_cell(n1=first_number,n2=second_number,op=operation)
            print(f"{first_number:.2f} {operation} {second_number:.2f} = {final_answer}")
            is_calculating = continue_calculating(result=final_answer)
        except TypeError as e:
            print(f"An error occured {e}")
        except ValueError as e:
            print(f"An error occured {e}")
        except KeyboardInterrupt:
            print("Keyboard exit!")
            quit()

    print("Thank you for using our program!\nGood bye")

if __name__ == "__main__":
    main()