import time, math
from datetime import date
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
MONTH_TO_DAYS = {
    1: 31,
    2: 31+28,
    3: 31+28+31,
    4: 31+28+31+30,
    5: 31+28+31+31,
    6: 31+28+31+31+30,
    7: 31+28+31+31+30+31,
    8: 31+28+31+31+30+31+31,
    9: 31+28+31+31+30+31+31+30,
    10: 31+28+31+31+30+31+31+30+31,
    11: 31+28+31+31+30+31+31+30+31+30,
    12: 31+28+31+31+30+31+31+30+31+30+31,
}

while True:
    #* ask for year *#
    year = 0
    while year <= 0 or year > date.today().year:
        try:
            year = int(input(Fore.BLUE + 'please enter the object\'s year of creation: '))
            
            if year == 0:
                print(Fore.RED + 'there\'s no such thing as a year 0')
            if year < 0:
                print(Fore.RED + 'you can\'t enter a negative year')
            if year > date.today().year:
                print(Fore.RED + 'you can\'t be born in the future')
        except:
            print(Fore.RED + 'please enter a number for year')
    print('year of creation set!')
    print('\033c', end='') # clear terminal

    #* ask for month *#
    month = 0
    while month <= 0 or month > 12: # month must be between 1 and 12
        try:
            month = int(input(Fore.YELLOW + 'please enter the object\'s month of creation: '))
            
            if month == 0:
                print(Fore.RED + 'there\'s no such thing as a month 0')
            if month < 0:
                print(Fore.RED + 'there\'s no such thing as a negative month')
            if month >= 12:
                print(Fore.RED + 'there\'s only 12 months')
        except:
            print(Fore.RED + 'please enter a number for month')
    print('month of creation set!')
    print('\033c', end='') # clear terminal

    #* ask for day *#
    MAX_DAYS = 0
    match month: # finds how many days in month
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
            day = int(input(Fore.CYAN + 'please enter the object\'s day of creation: '))
            
            if day == 0:
                print(Fore.RED + 'there\'s no such thing as a day 0')
            if day < 0:
                print(Fore.RED + 'there\'s no such thing as a negative day')
            if day >= MAX_DAYS:
                print(Fore.RED + f'there\'s only {MAX_DAYS} days in {MONTH_TO_STR[month]}')
        except:
            print(Fore.RED + 'please enter a number for day')
    print('day of creation set!')
    print('\033c', end='') # clear terminal

    #* lists age of thing *#
    current_date = date.today()

    TimeExisting = [0, 0, 0] # declares array containing no. of years, months, and days

    # checks if birthday has been passed or not
    if current_date.month >= month and current_date.day >= day:
        # difference between current year and year of birth 
        TimeExisting[0] = current_date.year - year 
    else:
        # subtracts one if birthday has not passed this year
        TimeExisting[0] = (current_date.year - year)-1 
    
    # checks if day of birth has been passed or not
    if current_date.day >= day:
        # difference between current month and month of birth
        TimeExisting[1] = current_date.month - month 
    else:
        # subtracts one if month has not passed the day
        TimeExisting[1] = (current_date.month - month)-1

    # adds twelve to months existing if negative
    if TimeExisting[1] < 0:
        TimeExisting[1] = 12 + TimeExisting[1]
    
    MAX_DAYS_MONTH_BEFORE_CURRENT = 0
    match current_date.month - 1: # finds max days of month before current month
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: # months with 31 days
            MAX_DAYS_MONTH_BEFORE_CURRENT = 31
        case 4 | 6 | 9 | 11: # months with 30 days
            MAX_DAYS_MONTH_BEFORE_CURRENT = 30
        case 2: # february
            if year % 4 == 0: # leap years
                MAX_DAYS_MONTH_BEFORE_CURRENT = 29
            else:
                MAX_DAYS_MONTH_BEFORE_CURRENT = 28

    # finds difference between current day and day of birth
    TimeExisting[2] = current_date.day - day
    # adds twelve to days existing if negative
    if TimeExisting[2] < 0: 
        TimeExisting[2] = MAX_DAYS_MONTH_BEFORE_CURRENT + TimeExisting[2]

    # 12 months per year + remaining months
    TOTAL_MONTHS = (TimeExisting[0] * 12) + TimeExisting[1]
    
    # 365.25 days per year + average of 30.438 days per month + remaining days
    TOTAL_DAYS = round(TimeExisting[0] * 365.25 + TimeExisting[1] * 30.438 + TimeExisting[2])

    print(Fore.MAGENTA + f'this thing came to be on {Fore.GREEN}{year}/{month}/{day}\n')
    print(Fore.MAGENTA + 'how long has this thing existed for?')
    print(Fore.MAGENTA + f'it has existed for {Fore.GREEN}{TimeExisting[0]} years {TimeExisting[1]} months and {TimeExisting[2]} days')
    print(Fore.MAGENTA + f'a total of {Fore.GREEN}{TOTAL_MONTHS} months')
    print(Fore.MAGENTA + f'a total of {Fore.GREEN}{TOTAL_DAYS} days (estimate)')

    input(Fore.MAGENTA + '~~> ')

    print('\033c', end='') # clear terminal
    
    
