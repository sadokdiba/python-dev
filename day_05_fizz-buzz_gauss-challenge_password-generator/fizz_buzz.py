import time

def main():  
    try:
        attempts = 2
        while True:
            number_entered = int(input("Enter a number between 10 and 100\n"))
            if 10 <= number_entered < 100:
                process_number(number_entered)
            elif attempts == 0:
                print("Attempts exhausted! Good bye")
                quit()
            else:
                print(f"Number out of range, attemps left {attempts}")
                attempts-=1
                continue
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye")
    except Exception as e:
        print(f"An error occured: {e} - restart program and try again")
        quit()

       
def process_number(number_entered):
    lower_range=1
    upper_range = number_entered + 1 # the 1 is there just to make up for counting all the way to max chosen number

    for number in range(lower_range,upper_range):

        if number%3 == 0 and number%5 == 0:
            number = "FizzBuzz"
            print(f"\n{number}")

        elif number%3 == 0:
            number = "Fizz"
            print(f"\n{number}")

        elif number%5 == 0:
            number = "Buzz"
            print(f"\n{number}")
        else:
            print(f"\n{number}")
        time.sleep(1)
    quit()
    
if __name__ == "__main__":
    main()