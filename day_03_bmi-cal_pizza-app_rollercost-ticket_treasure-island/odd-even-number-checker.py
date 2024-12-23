import time

print("This program checks whether the number is Even or Odd")

def final_answer(number_entered):
    '''This calculates the final answer'''
    number_entered_divby_2 = float(number_entered /2) 
    print(f"Because {number_entered} divided by 2 is equal to {number_entered_divby_2:.2f}, has a remainder of {number_entered%2}")

def main():
    '''This is the main function'''
    while True:
        try:
            number_entered = int(input("Please enter the number you would like to check: "))
            result = (number_entered % 2)

            if result == 0:
                print(f"The number {number_entered} is an even number")
            else:
                print(f"The number {number_entered} is an odd number")
            time.sleep(1)
            final_answer(number_entered)
            another_attempt = input("Would you like to check another number [y/n]? :").strip().lower()
            if another_attempt == "y":
                continue
            elif another_attempt == "n":
                print("Thanks for playing, good bye")
                break
            else:
                print("Invalid input, try again later")
                quit()
        except KeyboardInterrupt:
            print("Program terminated, good bye")
            quit()
        except ValueError as e:
            print(f"An error occured: {e}")
            quit()
if __name__ == "__main__":
    main()