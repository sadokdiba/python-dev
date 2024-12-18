import time
print("Welcome to the rollercoaster!")
time.sleep(1)

def agechecker():
    age = int(input("Please enter your age? "))
    if age <= 12:
        print("you can ride the rollercoaster and you will pay $5")
    elif age <= 18:
        print("you can ride the rollercoaster and you will pay $10")
    else:
        print("you can ride the rollercoaster and you will pay $15")

def main():
    height = int(input("Please enter your height: "))
    if height > 120:
        agechecker()
    else:
        print("Sorry you cannot ride the rollercoaster")

if __name__== "__main__":
    main()
