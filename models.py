from datetime import date
from decimal import Decimal

from exceptions import ExceptionMessage


class Expense:
    def __init__(
        self,
        amount: Decimal,
        date: date,
        description: str,
        category: str,
    ) -> None:
        if amount <= 0:
            raise ExceptionMessage("Enter posetive number for amount")
        description = description.strip()
        category = category.strip()
        if category.isspace():
            raise ExceptionMessage("The category doesn't have to have space!")
        if description.isspace():
            raise ExceptionMessage("The description doesn't have to have space!")
        self.amount = amount
        self.date = date
        self.description = description
        self.category = category
