"""
Lab1Q1 - Justin Third - 8/23/2023
first project, both my pycharm, python, and git melted down in class. I'm quite lucky I even built this one
I realize I capital cased my variables, I will use camel case going forward

    References:
    1 = https://automatetheboringstuff.com/2e/chapter8/
    2 = https://www.askpython.com/python/examples/obtain-current-year-and-month#:~:text=In%20Python%2C%20you%20can%20obtain,function%20to%20format%20the%20output.
"""

import pyinputplus as pyip
from datetime import datetime


def main():
    # Testing new features I am researching, added all versions of the month
    month_dictionary = {
        1: {"full": "January", "abbreviated": "Jan"},
        2: {"full": "February", "abbreviated": "Feb"},
        3: {"full": "March", "abbreviated": "Mar"},
        4: {"full": "April", "abbreviated": "Apr"},
        5: {"full": "May", "abbreviated": "May"},
        6: {"full": "June", "abbreviated": "Jun"},
        7: {"full": "July", "abbreviated": "Jul"},
        8: {"full": "August", "abbreviated": "Aug"},
        9: {"full": "September", "abbreviated": "Sep"},
        10: {"full": "October", "abbreviated": "Oct"},
        11: {"full": "November", "abbreviated": "Nov"},
        12: {"full": "December", "abbreviated": "Dec"}
    }


    UserName = input("Please enter your preferred name: ")

    #  Added 8/29
    while not UserName or UserName in ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '~', '/',
                                       '\\', '|', ':', ';', '"', '<', '>', '?']:
        UserName = input("Your name cannot be blank or include unauthorized characters,\n Please enter your name: ")

    NameLength = len(UserName.replace(" ", ""))

    # Testing a new method of this step, 8/29
    # UserMonth = pyip.inputNum("Please enter the month of your birth (Number of Month Accepted): ")  # 1
    #
    # while int(UserMonth) < 1 or int(UserMonth) > 12:
    #     UserMonth = input("Please enter the month between 1 and 12 (Number of Month Accepted): ")

    UserMonth = input("Please enter the month of your birth: ")
    UserMonth = UserMonth.capitalize()

    if UserMonth.isdigit():
        while int(UserMonth) < 1 or int(UserMonth) > 12:
            UserMonth = input("Please enter the month between 1 and 12 (Number of Month Accepted): ")

    # for NumMonth in month_dictionary.items():
    if UserMonth.isdigit():
        UserMonth = month_dictionary[int(UserMonth)]["full"]
        print(UserMonth)
    else:
        if UserMonth in month_dictionary:
            print(UserMonth)

    print(f'Initializing User: {UserName}!')
    print(f'Letter count of User Name: {NameLength}')

    ThisMonth = datetime.now().month  # 2

    if ThisMonth == UserMonth:
        print(f'{UserName}, it is your birthday month: {UserMonth}')
    else:
        print(f'{UserName}, It is not your birthday month. Birth: {UserMonth} '
              f'VS Current: {month_dictionary[int(ThisMonth)]["full"]}')

if __name__ == '__main__':
    main()
