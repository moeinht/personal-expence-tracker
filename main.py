import datetime
from decimal import Decimal
import decimal

from exceptions import ExceptionMessage
from models import Expense


def display_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Reports")
    print("0. Exit")


def add_expense():
    print("Add Expense selected")
    a = Expense(
        amount=Decimal("-22.2"),
        date=datetime.datetime.now(),
        category="t",
        description="lvld lkdfvlkdl",
    )


def view_expenses():
    print("View Expenses selected")


def view_reports():
    print("View Reports selected")


def main():
    actions = {1: add_expense, 2: view_expenses, 3: view_reports}

    while True:
        try:
            display_menu()
            user_input = int(input("Enter one of the options here:"))

            if not user_input:
                print("Good Byyyyy")
                break

            action = actions.get(user_input)

            if action is None:
                print("Please enter value between (1,2,3,0)")
                continue

            action()

        except ValueError:
            print("Enter correct value!")
        except ExceptionMessage as e:
            print(str(e))


if __name__ == "__main__":
    main()
