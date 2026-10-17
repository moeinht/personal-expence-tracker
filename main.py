import datetime
from decimal import Decimal, InvalidOperation

from models import Expense
from reports import total_expenses
from tracker import ExpenseTracker

tracker = ExpenseTracker()


def display_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Reports")
    print("0. Exit")


def get_category() -> str:
    categories = tracker.categories

    if not categories:
        return get_non_empty_text("Enter a new category: ")

    print("\n=== Existing Categories ===")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    print("0. Add a new category")

    while True:
        choice = input("Choose a category number or enter 0 for a new one: ").strip()

        if choice == "0":
            return get_non_empty_text("Enter a new category: ")

        try:
            index = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= index <= len(categories):
            return categories[index - 1]

        print("Invalid category number. Try again.")


def get_non_empty_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()

        if not value:
            print("This field cannot be empty. Please try again.")
            continue

        return value


def get_amount() -> Decimal:
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


def add_expense():
    category = get_category()
    amount = get_amount()
    description = get_non_empty_text("Enter description: ")

    expense = Expense(
        amount=amount,
        date=datetime.datetime.now(),
        category=category,
        description=description,
    )

    tracker.add_expense(expense)
    print("Expense added successfully!")


def view_expenses():
    if not tracker.expenses:
        print("No expenses found.")
        return

    print("\n=== Your Expenses ===")

    for index, expense in enumerate(tracker.expenses, start=1):
        print(f"\nExpense #{index}")
        print(f"Amount: {expense.amount:.2f}")
        print(f"Date: {expense.date}")
        print(f"Category: {expense.category}")
        print(f"Description: {expense.description}")


def view_reports():
    total = total_expenses(tracker.expenses)

    print("\n=== Expense Reports ===")
    print(f"Total expenses: {total:.2f}")


def main():
    actions = {
        1: add_expense,
        2: view_expenses,
        3: view_reports,
    }

    while True:
        display_menu()

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if choice == 0:
            print("Goodbye!")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid option. Choose 0, 1, 2, or 3.")
            continue

        action()


if __name__ == "__main__":
    main()
