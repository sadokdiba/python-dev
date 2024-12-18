import time

weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))

try:
    weight = float(input("Please enter your weight in kilograms \n"))
    height = float(input("Please enter your height in in meters eg. 1.75m \n"))
except:
    print("Enter a valid number")
    quit()
bmi_calculation = weight/height**2

if bmi_calculation < 18.5:
    print(f"Your BMI is {round(bmi_calculation)} and you are underweight")
elif 18.5 < bmi_calculation < 25:
    print(f"Your BMI is {round(bmi_calculation)} and your weight is normal")
else:
    print(f"Your BMI is {round(bmi_calculation)} and you are overweight")