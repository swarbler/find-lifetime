import time
import datetime
from colorama import Fore, Back

MONTH_TO_STR = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december',
}

while True:
    year = 0
    while year <= 0 or year > datetime.date.today().year:
        try:
            year = int(input(Fore.BLUE + 'please enter your year of birth: '))
            
            if year == 0:
                print(Fore.RED + 'there\'s no such thing as a year 0')
            if year < 0:
                print(Fore.RED + 'you can\'t enter a negative year')
            if year > datetime.date.today().year:
                print(Fore.RED + 'you can\'t be born in the future')
        except:
            print(Fore.RED + 'please enter a number for year')
    print('year of birth set!')
    print('\033c', end='') # clear terminal

    month = 0
    while month <= 0 or month > 12: # month must be between 1 and 12
        try:
            month = int(input(Fore.YELLOW + 'please enter your month of birth: '))
            
            if month == 0:
                print(Fore.RED + 'there\'s no such thing as a month 0')
            if month < 0:
                print(Fore.RED + 'there\'s no such thing as a negative month')
            if month >= 12:
                print(Fore.RED + 'there\'s only 12 months')
        except:
            print(Fore.RED + 'please enter a number for month')
    print('month of birth set!')
    print('\033c', end='') # clear terminal

    # sets maximum number of days
    MAX_DAYS = 0
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: # months with 31 days
            MAX_DAYS = 31
        case 4 | 6 | 9 | 11: # months with 30 days
            MAX_DAYS = 30
        case 2: # february
            if year % 4 == 0: # leap years
                MAX_DAYS = 29
            else:
                MAX_DAYS = 28

    day = 0
    while day <= 0 or month > MAX_DAYS: # month must be between 1 and MAX_DAYS
        try:
            day = int(input(Fore.GREEN + 'please enter your day of birth: '))
            
            if day == 0:
                print(Fore.RED + 'there\'s no such thing as a day 0')
            if day < 0:
                print(Fore.RED + 'there\'s no such thing as a negative day')
            if day >= MAX_DAYS:
                print(Fore.RED + f'there\'s only {MAX_DAYS} days in {MONTH_TO_STR[month]}')
        except:
            print(Fore.RED + 'please enter a number for day')
    print('day of birth set!')
    print('\033c', end='') # clear terminal
