def is_leap_year(year):
    '''Check if year is leap'''
    if year % 4 == 0 and year % 20 == 0 and year % 400 == 0:
        return year == year
    return False

attempts = 3
while attempts > 0:
    try:
        year_inputed = int(input("Enter the year you'd like to determine: \n"))
        if year_inputed > 0:
            is_year_leap = is_leap_year(year=year_inputed)
            print(is_year_leap)
            print(is_leap_year.__doc__)
            quit()
        elif year_inputed < 0:
            print("Please enter a positive year number")
            attempts -=1
        else:
            print(f"{ValueError}")
    except KeyboardInterrupt:
        print("Program ended.")
        quit()
    except ValueError as e:
        print(f"An error occurred: {e}")
        attempts -=1
print("Too many invalid entries, try again")