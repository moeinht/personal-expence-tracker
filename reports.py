import csv
import os
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from models import Expense

EXPORTS_PATH = Path(__file__).parent / "exports"


def total_expenses(expenses: list[Expense]) -> Decimal:
    total = Decimal("0")

    for expense in expenses:
        total += expense.amount

    return total


def export_file(expenses: list[Expense]):
    if not EXPORTS_PATH.exists():
        os.makedirs(EXPORTS_PATH)

    with open(f"./exports/export_{datetime.now()}.csv", "w", newline="") as file:
        writter = csv.writer(file)
        writter.writerow("amount,date,category,description".split(","))

        for expense in expenses:
            writter.writerow(
                [
                    f"{expense.amount}",
                    f"{expense.date}",
                    expense.category,
                    expense.description,
                ]
            )
