# region lottery-date
import calendar
import datetime
import random


def generate_date():
    """The user enters two dates in the format YYYY-MM-DD.
    The program generates a random date between the two dates."""
    # Get two dates from the user input
    while True:
        try:
            date1 = input("Enter the first date in YYYY-MM-DD format: ")
            date1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid input. Please try again.")

    while True:
        try:
            date2 = input("Enter the second date in YYYY-MM-DD format: ")
            date2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
            # Check if date1 is not greater than date2
            if date2 > date1:
                break
            else:
                print("The second date must be later than the first date. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    # Generate a random date between the two dates
    delta = date2 - date1
    random_days = datetime.timedelta(days=random.randint(0, delta.days))
    new_date = date1 + random_days

    # Check if the new date is on a Monday
    if calendar.day_name[new_date.weekday()] == 'Monday':
        print(f"The new date is {new_date.strftime('%Y-%m-%d')}" + " I have no vinegar!")
    else:
        print(f"The new date is {new_date.strftime('%Y-%m-%d')}")


# endregion