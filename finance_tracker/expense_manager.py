"""
expense_manager.py
Manages all expense operations.
"""

from collections import defaultdict
from .expense import Expense


class ExpenseManager:

    def __init__(self):
        self.expenses = []
        self.budget = 0

    # -----------------------------
    # Expense Operations
    # -----------------------------

    def add_expense(self, expense):

        if not isinstance(expense, Expense):
            raise TypeError("Only Expense objects are allowed.")

        self.expenses.append(expense)

    def remove_expense(self, index):

        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense index.")

        del self.expenses[index]

    def get_all_expenses(self):
        return self.expenses

    def clear_all(self):
        self.expenses.clear()

    # -----------------------------
    # Search
    # -----------------------------

    def search_description(self, keyword):

        keyword = keyword.lower()

        return [
            expense
            for expense in self.expenses
            if keyword in expense.description.lower()
        ]

    # -----------------------------
    # Filters
    # -----------------------------

    def filter_category(self, category):

        category = category.title()

        return [
            expense
            for expense in self.expenses
            if expense.category == category
        ]

    def filter_date(self, date):

        return [
            expense
            for expense in self.expenses
            if expense.date == date
        ]

    def filter_month(self, month):

        """
        month example:
        2026-08
        """

        return [
            expense
            for expense in self.expenses
            if expense.date.startswith(month)
        ]

    # -----------------------------
    # Totals
    # -----------------------------

    def total_expense(self):

        return sum(expense.amount for expense in self.expenses)

    def monthly_total(self, month):

        return sum(
            expense.amount
            for expense in self.filter_month(month)
        )

    # -----------------------------
    # Category Summary
    # -----------------------------

    def category_summary(self):

        summary = defaultdict(float)

        for expense in self.expenses:
            summary[expense.category] += expense.amount

        return dict(summary)

    # -----------------------------
    # Monthly Summary
    # -----------------------------

    def monthly_summary(self):

        summary = defaultdict(float)

        for expense in self.expenses:
            month = expense.date[:7]
            summary[month] += expense.amount

        return dict(summary)

    # -----------------------------
    # Budget
    # -----------------------------

    def set_budget(self, amount):

        amount = float(amount)

        if amount <= 0:
            raise ValueError("Budget must be positive.")

        self.budget = amount

    def remaining_budget(self):

        return self.budget - self.total_expense()

    def budget_status(self):

        if self.budget == 0:
            return "Budget not set."

        remaining = self.remaining_budget()

        if remaining >= 0:
            return f"Remaining Budget : ₹{remaining:.2f}"

        return f"Budget Exceeded by ₹{abs(remaining):.2f}"

    # -----------------------------
    # Recurring Expenses
    # -----------------------------

    def recurring_expenses(self):

        recurring = []

        descriptions = defaultdict(int)

        for expense in self.expenses:
            descriptions[expense.description] += 1

        for expense in self.expenses:
            if descriptions[expense.description] > 1:
                recurring.append(expense)

        return recurring

    # -----------------------------
    # Prediction
    # -----------------------------

    def predict_next_month(self):

        monthly = self.monthly_summary()

        if len(monthly) == 0:
            return 0

        return round(sum(monthly.values()) / len(monthly), 2)

    # -----------------------------
    # Statistics
    # -----------------------------

    def statistics(self):

        if not self.expenses:

            return {
                "count": 0,
                "total": 0,
                "average": 0,
                "highest": 0,
                "lowest": 0
            }

        amounts = [expense.amount for expense in self.expenses]

        return {

            "count": len(amounts),

            "total": sum(amounts),

            "average": round(sum(amounts) / len(amounts), 2),

            "highest": max(amounts),

            "lowest": min(amounts)

        }

    