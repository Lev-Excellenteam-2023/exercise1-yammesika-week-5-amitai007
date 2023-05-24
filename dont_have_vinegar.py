# region lottery-date
import calendar
import datetime
import random

def check_dates(first_date, second_date):
    # Check if first_date is not greater than second_date
    if second_date > first_date:
        return True
    else:
        return False
    

def generate_date(first_date, second_date):
    """The user enters two dates in the format YYYY-MM-DD.
    The program generates a random date between the two dates."""
    # Generate a random date between the two dates
    delta = second_date - first_date
    random_days = datetime.timedelta(days=random.randint(0, delta.days))
    new_date = first_date + random_days

    # Check if the new date is on a Monday
    if calendar.day_name[new_date.weekday()] == 'Monday':
        return f"The new date is {new_date.strftime('%Y-%m-%d')}" + " I have no vinegar!"
    else:
        return f"The new date is {new_date.strftime('%Y-%m-%d')}"


# endregion


if __name__ == '__main__':
    
    # Get two dates from the user input
    first_date = input("Enter the first date in YYYY-MM-DD format: ")
    first_date = datetime.datetime.strptime(first_date, '%Y-%m-%d').date()
    second_date = input("Enter the second date in YYYY-MM-DD format: ")
    second_date = datetime.datetime.strptime(second_date, '%Y-%m-%d').date()
    
    # Check if first_date is not greater than second_date 
    flag = check_dates(first_date, second_date)
    if flag == True:
        generate_date(first_date, second_date)
    else:
        print("The second date must be later than the first date. Please try again.")
    
    
       
