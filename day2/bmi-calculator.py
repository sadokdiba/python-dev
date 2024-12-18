import time
print("This is a calculator to help you calculate your BMI")
time.sleep(1)

try:
    weight = float(input("Please enter your weight in kilograms \n"))
    height = float(input("Please enter your height in in meters eg. 1.75m \n"))
except:
    print("Enter a valid number")
    quit()

bmi_calculation = weight/height**2

print("Calculating...")
time.sleep(3) #pretending to calculate :)

print("Your BMI is:", round(bmi_calculation))