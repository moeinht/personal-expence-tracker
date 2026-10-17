from datetime import date
from decimal import Decimal


class Expense:
    def __init__(
        self,
        amount: Decimal,
        date: date,
        description: str,
        category: str,
    ) -> None:

        self.amount = amount
        self.date = date
        self.description = description
        self.category = category
