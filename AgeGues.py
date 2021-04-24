Current_year = 2021

user_age = input("Enter your current age as of today of your year of birth: ")

while (4 >= len(user_age) > 0) and int(user_age)>0:

    if len(user_age) < 4:
        Calculated_yob = Current_year - (int(user_age))
        Calculated_age=int(user_age)
        print(f"You were born in {Calculated_yob}")
    else:
        Calculated_age = Current_year - (int(user_age))
        Calculated_yob=int(user_age)
        print(f"You are {Calculated_age} years old as of today")

        if Calculated_yob < 1900:
            print("You should be dead by now")
        elif Calculated_age<0:
            print("Welcome from future, Alien ")
        elif Calculated_age>100:
            print("Wow, you could be the oldest person alive")

    guess_age=int(input("Enter the year you want to see age of :"))
    difference=guess_age-Current_year
    print(f"You will be {(Calculated_age+difference)} years old in {guess_age} ")
    choice = input("Enter C to Continue and Q to Quit")
    if choice == 'c' or 'C':
        continue
    elif choice == 'q' or 'Q':
        break


print("Invalid Entry")
