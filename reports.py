from decimal import Decimal

from models import Expense


def total_expenses(expenses: list[Expense]) -> Decimal:
    total = Decimal("0")

    for expense in expenses:
        total += expense.amount

    return total
