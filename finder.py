from datetime import datetime, date
from colorama import Fore, Back

def calculate_age(birthday):
    # get today's date
    today = date.today()
    
    # calculate the difference in days
    delta = today - birthday
    
    # calculate years
    years = today.year - birthday.year
    
    # adjust years if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthday.month, birthday.day):
        years -= 1
    
    # calculate the remaining months and days
    if today.month >= birthday.month:
        months = today.month - birthday.month
    else:
        months = 12 + today.month - birthday.month
    
    if today.day >= birthday.day:
        days = today.day - birthday.day
    else:
        # handle the case where today's day is less than the birthday's day
        # by subtracting one month and adding the appropriate number of days
        months -= 1
        days = (today - date(today.year, today.month - 1, birthday.day)).days
    
    return years, months, days, delta.days

while True:
    # prompt the user for their birthday
    birthday_str = input(Fore.BLUE + 'Enter your birthday (YYYY-MM-DD): ' + Fore.CYAN)
    
    try:
        # convert the input string to a date object
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
        
        # calculate the age
        years, months, days, total_days = calculate_age(birthday)
        
        # output the result
        print(f'You have lived for {years} years, {months} months, and {days} days.')
        print(f'Total days lived: {total_days}')
    
    except ValueError:
        print('Invalid date format. Please enter the date in YYYY-MM-DD format.')
    
    print(Fore.RED)
    print('enter "y" if you would like to find the lifetime of another object')
    userInput = input('~~> ').lower().strip()

    if userInput != 'y':
        break

    print('\033c', end='') # clear terminal
