from models import Expense
from storage import load_expenses, save_expense


class ExpenseTracker:
    def __init__(self):
        self.expenses, self.categories = load_expenses()

    def add_expense(self, expense: Expense) -> None:
        save_expense(expense)
        self.expenses.append(expense)

        if expense.category not in self.categories:
            self.categories.append(expense.category)
            self.categories.sort()
