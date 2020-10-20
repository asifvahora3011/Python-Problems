'''Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like:                       (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!'''

def age():
    user = input("Enter your age or year of birth:")
    initial= user
    def birth():
        optional = input("Enter a year you wish to know your age in:")
        age_in_year = int(optional) - int(initial)
        print(f"Your age in {optional} will be {age_in_year} years.")
    def perticular_age():
        y_n = input("Would you like know your age in any perticular year? Y or N:")
        if y_n == "Y":
            optional = input("Enter a year you wish to know your age in:")
            age_in_year = int(optional) - int(initial)
            print(f"Your age in {optional} will be {age_in_year} years.")
        elif y_n == "N":
            exit()
        else:
            print("Invalid input!")
    if int(user) > 2020:
        print("You are not born yet. Enter a valid year")
        age()
    else:
        if len(user) == 4:
            print("You have entered your birth year.")
            year_century = int(initial) + 100
            print(f"You'll turn 100 years old in year {year_century}")
            perticular_age()
        elif len(user) <= 3:
            print("You have entered your age.")
            if int(user) > 100:
                print("You are seem to be the oldest person alive!")
            elif int(user) < 100:
                age_century = 100 - int(initial)
                print(f"You'll turn 100 years old after {age_century} years.")
            elif int(user) == 100:
                print("Congratulations! You are 100 years old.")
            optional1=input("If you wish to know your age in any perticular year, please enter your birth year:")
            initial = optional1
            birth()
        else:
            print("Your input must be 2 or 4 numbers long.")
age()


