print("Welcome to the tip calculator!")
try:
    bill_total = float(input("What was the total of the bill? $"))
except:
    print("Please enter a number")
    quit()
tip_percent_amount = float(input("How much tip would you like to give in %? 10, 12 or 15? "))
split_bill_number = int(input("How many people to split the bill? "))
final_amount_per_person = (((bill_total*tip_percent_amount)/100) + bill_total) /split_bill_number
rounded_final_amount_per_person = round(final_amount_per_person,2)
print(f"Each person should pay: $ {rounded_final_amount_per_person:.2f}")