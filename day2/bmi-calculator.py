import time
print("This is a calculator to help you calculate your BMI")
time.sleep(1)
weight = float(input("Please enter your weight in kilograms \n"))
height = float(input("Please enter your height in in meters eg. 1.75m \n"))
bmi_calculation = weight/height**2
print("Calculating...")
time.sleep(3) #pretending to calculate :)
print(f"Your BMI is {bmi_calculation:.2f}")