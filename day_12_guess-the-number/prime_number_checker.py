def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True

number = int(input("Please enter the number you would like to check: "))

result = is_prime(number)
if result == True:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
