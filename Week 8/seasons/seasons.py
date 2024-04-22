# calculate minutes since you were born from  birthdate
import sys
import re
from datetime import date
import inflect
p = inflect.engine()


def main():
    user_bday = input("Date of Birth: ")
    print((f"{calculate(user_bday)} minutes").capitalize())


def calculate(user_bday):
    try:
        birthday = date.fromisoformat(user_bday)
        today = date.today()
        age = today - birthday
        minutes = p.number_to_words(age.days * 24 * 60, andword="")

        return(minutes)

    except ValueError:
        exit('Invalid date')


if __name__ == "__main__":
    main()
