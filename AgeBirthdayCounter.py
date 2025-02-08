# Week 2 lab
'''Age Calculator with Birthday Countdown'''

import datetime

birth_year = 0
birth_month = 0
birth_day = 0
birth_leap_new_day = 0

month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

number_of_days = 0
month_days_copy = {}

date_today = datetime.date.today()
today_year = date_today.year
today_month = date_today.month
today_day = date_today.day

while not birth_year:
    try:
        birth_year = int(input("Enter 4-digit year of birth, enter 0 to exit: "))
        if not birth_year:
            birth_year = 0
            print("Existing the program...")
            break
    except ValueError:
        print("Please enter a number for the year of birth, try again or enter 0 to exit.")
        birth_year = 0
    except Exception as err:
        birth_year = 0
        print(f"Unexpected {err=} occurred: {type(err)=}")
        raise
    else:
        if (birth_year > today_year) or (birth_year < 1):
            birth_year = 0
            print("Year of birth cannot be greater than current year or cannot be a negative value, try again or enter 0 to exit.")
    finally:
        print ("Year of birth is validated!")

if birth_year:
    while not birth_month:
        try:
            birth_month = int(input("Enter 1 or 2 digit month of birth (1 for Jan, 2 for Feb, ..., 12 for Dec): "))
            if not birth_month:
                birth_month = 0
                print("Existing the program...")
                break
        except ValueError:
            print("Please enter a number for the month of birth, try again or enter 0 to exit.")
            birth_month = 0
        except Exception as err:
            birth_month = 0
            print(f"Unexpected {err=} occurred: {type(err)=}")
            raise
        else:
            if (birth_month > 12) or (birth_month < 1):
                birth_month = 0
                print("Month of birth must be between 1 and 12, try again or enter 0 to exit.")
            elif ((birth_year == today_year) and (birth_month > today_month)):
                birth_month = 0
                print("Month of birth cannot be greater than current year, current month or cannot be a negative value, must be between 1 and 12, try again or enter 0 to exit.")
        finally:
            print("Month of birth is validated!")

if birth_year and birth_month:
    while not birth_day:
        try:
            birth_day = int(input("Enter the day of birth (1 through 31): "))
            if not birth_day:
                birth_day = 0
                print("Existing the program...")
                break
        except ValueError:
            print("Please enter a number for the day of birth, try again or enter 0 to exit.")
            birth_day = 0
        except Exception as err:
            birth_day = 0
            print(f"Unexpected {err=} occurred: {type(err)=}")
            raise
        else:
            if (birth_day > 31) or (birth_day < 1):
                birth_day = 0
                print("Day of birth must be between 1 and 31, try again or enter 0 to exit.")
            elif ((birth_year == today_year) and (birth_month == today_month) and (birth_day > today_day)):
                birth_day = 0
                print("Day of birth cannot be greater than current year, current month, try again or enter 0 to exit.")
            elif (not(birth_year % 4) and birth_month == 2 and birth_day == 29):
                    birth_leap_new_day = birth_day
                    break
            elif (birth_day > month_days[birth_month]):
                birth_day = 0
                print("Number of days should be valid for the month entered, try again or enter 0 to exit.")
        finally:
            print("Day of birth is validated!")

if birth_year and birth_month and birth_day:

    print("Birth's date: ", str(birth_year).rjust(4, '0')+'-'+str(birth_month).rjust(2, '0')+'-'+str(birth_day).rjust(2,'0'))
    print("Today's date: ", str(today_year).rjust(4, '0')+'-'+str(today_month).rjust(2, '0')+'-'+str(today_day).rjust(2,'0'))

    if (birth_year == today_year) and (birth_month == today_month) and (today_day >= birth_day):
        age = today_day - birth_day
        if age == 1:
            print(f"Age, as of today, is {age} day.")
        else:
            print(f"Age, as of today, is {age} days.")
    elif ((birth_year == today_year) and (today_month - birth_month == 1) and (today_day <= birth_day)):
        age = month_days[birth_month] - birth_day + today_day - 1
        if age == 1:
            print(f"Age, as of today, is {age} day.")
        else:
            print(f"Age, as of today, is {age} days.")
    elif (((today_year - birth_year) == 1) and (today_month - birth_month == -11) and (today_day <= birth_day)):
        age = month_days[birth_month] - birth_day + today_day
        if age == 1:
            print(f"Age, as of today, is {age} day.")
        else:
            print(f"Age, as of today, is {age} days.")
    elif (birth_year == today_year) and (today_month > birth_month):
        if (today_day > birth_day):
            age = today_month - birth_month
            if age == 1:
                print(f"Age, as of today, is {age} month.")
            else:
                print(f"Age, as of today, is {age} months.")
        else:
            age = today_month - birth_month - 1
            if age == 1:
                print(f"Age, as of today, is {age} month.")
            else:
                print(f"Age, as of today, is {age} months.")
    elif ((today_year - birth_year) == 1) and ((12 - (birth_month-today_month)) < 12):
        if (today_day > birth_day):
            age = 12 - (birth_month-today_month)
            if (age == 1):
                print(f"Age, as of today, is {age} month.")
            else:
                print(f"Age, as of today, is {age} months.")
        else:
            age = 12 - (birth_month-today_month) - 1
            if (age == 1):
                print(f"Age, as of today, is {age} month.")
            else:
                print(f"Age, as of today, is {age} months.")
    else:
        if (birth_month >= today_month):
            age = today_year - birth_year - 1
            if (age == 1):
                print(f"Age, as of today, is {age} year.")
            else:
                print(f"Age, as of today, is {age} years.")
        else:
            age = today_year - birth_year
            if (age == 1):
                print(f"Age, as of today, is {age} year.")
            else:
                print(f"Age, as of today, is {age} years.")

    if (birth_month == today_month) and (birth_day == today_day):
        number_of_days = -1
    elif (birth_month == today_month) and (birth_day > today_day):
        number_of_days = birth_day - today_day
    elif (birth_month > today_month) and ((birth_month - today_month) == 1):
        number_of_days = month_days[today_month] - today_day + birth_day
    if not((number_of_days == -1) or (number_of_days > 0)):
        for i in month_days:
            if (i < birth_month and i > today_month and birth_month > today_month) \
                or ((i < birth_month or i > today_month) and birth_month < today_month):
                month_days_copy[i] = month_days[i]
        if month_days_copy:
            for i, day_cnt in month_days_copy.items():
                number_of_days += day_cnt
            number_of_days += (month_days[today_month]-today_day+birth_day)
    if number_of_days > 0:
        number_of_days -= 1
    if ((today_year % 4 == 0) and (today_month <= 2) and birth_month > 2):
        number_of_days += 1
    elif ((today_year % 4 == 0) and (today_month <= 2) and birth_month == 2 and birth_day == 29):
        number_of_days += 1
    elif (today_month > 2) and (birth_month > 2 and ((today_year+1) % 4) == 0):
        number_of_days += 1
    elif (today_month > 2) and (birth_month == 2 and birth_day == 29) and (today_year+1 % 4 == 0):
        number_of_days += 1
    elif (birth_month == 2 and birth_day == 29):
        birth_leap_new_day = 28

    if (birth_leap_new_day != birth_day) and (birth_leap_new_day) and not(birth_year % 4) \
        and (birth_month == 2) and (birth_day == 29):
        print("It's not a leap year, you could celebrate your upcoming birthday on 28-Feb!")
        number_of_days -= 1

    if number_of_days == -1:
        print("It is your birth day today! Happy Birthday!")
    elif number_of_days == 0:
        print("It is your birth day tomorrow! Birthday wishes in advance!")
    else:
        print(f"Number of days until your birthday is {number_of_days}.")
