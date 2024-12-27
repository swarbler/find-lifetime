import time, math
from datetime import date
from colorama import Fore, Back

#* declares dictionaries *#
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


#* functions *#
def findDaysInMonth(param, year):
    """finds how many days are in the months"""
    match param: # finds max days of month before current month
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: # months with 31 days
            return 31
        case 4 | 6 | 9 | 11: # months with 30 days
            return 30
        case 2: # february
            if year % 4 == 0: # leap years
                return 29
            else:
                return 28
        case _: # invalid month
            return 30

def calculateMonths(param=[0,0,0]):
    """calculates number of months using years and months"""
    # 12 months per year + remaining months
    return (param[0] * 12) + param[1]

def estimateDays(param=[0,0,0]):
    """estimate number of days using years, months, and days given"""
    # 365.25 days per year + average of 30.438 days per month + remaining days
    return round(param[0] * 365.25 + param[1] * 30.438 + param[2])


#* program *#
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
            if month > 12:
                print(Fore.RED + 'there\'s only 12 months')
        except:
            print(Fore.RED + 'please enter a number for month')
    print('month of creation set!')
    print('\033c', end='') # clear terminal


    #* ask for day *#
    MAX_DAYS = findDaysInMonth(month, year)

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

    # years
    TimeExisting[0] = current_date.year - year 
    # subtracts years by 1 if birthday has not been passed yet
    if not(current_date.month >= month and current_date.day >= day): TimeExisting[0] -= 1 
    
    # months
    TimeExisting[1] = current_date.month - month 
    # subtracts months by 1 if day of birth has not been passed yet
    if not(current_date.day >= day): TimeExisting[1] -= 1

    # adds twelve to months if negative
    if TimeExisting[1] < 0: TimeExisting[1] += 12

    MAX_DAYS_MONTH_BEFORE_CURRENT = findDaysInMonth(current_date.month - 1, current_date.year)

    # days
    TimeExisting[2] = current_date.day - day

    # adds amount of days in month before current month to days existing if negative
    if TimeExisting[2] < 0: TimeExisting[2] += MAX_DAYS_MONTH_BEFORE_CURRENT

 
    TOTAL_MONTHS = calculateMonths(TimeExisting)
    TOTAL_DAYS = estimateDays(TimeExisting)

    print(Fore.MAGENTA + f'this thing came to be on {Fore.GREEN}{year}/{month}/{day}\n')
    print(Fore.MAGENTA + 'how long has this thing existed for?')
    print(Fore.MAGENTA + f'it has existed for {Fore.GREEN}{TimeExisting[0]} years {TimeExisting[1]} months and {TimeExisting[2]} days')
    print(Fore.MAGENTA + f'a total of {Fore.GREEN}{TOTAL_MONTHS} months')
    print(Fore.MAGENTA + f'a total of {Fore.GREEN}{TOTAL_DAYS} days (estimate)')
    input()

    print(Fore.RED)
    print('enter "y" if you would like to find the lifetime of another object')
    userInput = input('~~> ').lower()

    if userInput != 'y':
        break

    print('\033c', end='') # clear terminal
    
