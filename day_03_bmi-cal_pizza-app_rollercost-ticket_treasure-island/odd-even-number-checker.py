print("This program checks whether the number is Even or Odd")

number_entered = int(input("Please enter the number you would like to check: "))
result = (number_entered % 2)

if result == 0:
    print(f"The number {number_entered} is an even number")
else:
    print(f"The number {number_entered} is an odd number")
