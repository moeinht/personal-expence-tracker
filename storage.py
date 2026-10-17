import csv
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from models import Expense

DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"


def save_expense(expense: Expense) -> None:
    file_exists = DATA_FILE.exists()
    file_is_empty = not file_exists or DATA_FILE.stat().st_size == 0

    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file_is_empty:
            writer.writerow(["amount", "date", "category", "description"])

        writer.writerow(
            [
                str(expense.amount),
                expense.date.isoformat(),
                expense.category,
                expense.description,
            ]
        )


def load_expenses() -> tuple[list[Expense], list[str]]:
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return ([], [])

    expenses = []
    categories = set()

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense = Expense(
                amount=Decimal(row["amount"]),
                date=datetime.fromisoformat(row["date"]),
                category=row["category"],
                description=row["description"],
            )
            categories.add(expense.category)
            expenses.append(expense)

    return (expenses, sorted(categories))
