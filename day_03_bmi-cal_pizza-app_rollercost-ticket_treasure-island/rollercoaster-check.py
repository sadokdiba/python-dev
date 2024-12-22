import time
print("Welcome to the rollercoaster!")
time.sleep(1)

def photo_check(bill):
    attempts =3
    while attempts > 0:
        wants_photo = input("Do you want to have a photo taken? Type 'y' for Yes and 'n' for No: ").strip().lower()
        if wants_photo in ["y", "n"]:
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid input. Please type 'y' for Yes or 'n' for No.. {attempts} attempts left.")
            else:
                print("No attempts left. Exiting.")
                break
    
    if wants_photo == "y":
        bill += 3
    
    print(f"Your final bill is ${bill}")
    return bill

def agechecker():
    age = int(input("Please enter your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are  $5")

    elif age <= 18:
        bill = 10
        print("Youth tickets are $10")
    else:
        bill = 15
        print("adult tickets are $15")
    photo_check(bill)

def main():
    attempts = 3
    while attempts > 0:
        try:
            height = int(input("Please enter your height in cm: "))
            break
        except ValueError:
            attempts -= 1
            if attempts > 0:
                print(f"Please enter a valid height. {attempts} attempts left.")
            else:
                print("No attempts left. Exiting.")
                quit()
      
    if height > 120:
        agechecker()
    else:
        print("Sorry you cannot ride the rollercoaster")

if __name__== "__main__":
    main()
    
