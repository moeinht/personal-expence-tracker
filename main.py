import datetime
from decimal import Decimal, InvalidOperation

from models import Expense
from tracker import ExpenseTracker


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()

        if not value:
            print("This field cannot be empty. Please try again.")
            continue

        return value


def get_amount():
    while True:
        amount_input = input("Enter amount: ").strip()

        try:
            amount = Decimal(amount_input)
        except InvalidOperation:
            print("Invalid amount. Please enter a number.")
            continue

        if not amount.is_finite():
            print("Amount must be a finite number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return amount


def display_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Reports")
    print("0. Exit")


def add_expense():
    category = get_non_empty_text("Enter category: ")
    amount = get_amount()
    description = get_non_empty_text("Enter description: ")

    expense = Expense(
        amount=amount,
        date=datetime.datetime.now(),
        category=category,
        description=description,
    )

    print("Expense created successfully!")


def view_expenses():
    print("View Expenses selected")


def view_reports():
    print("View Reports selected")


def main():
    actions = {1: add_expense, 2: view_expenses, 3: view_reports}
    tracker = ExpenseTracker()

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


if __name__ == "__main__":
    main()
