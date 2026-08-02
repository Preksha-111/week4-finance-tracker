"""
expense.py
Defines the Expense class used throughout the Personal Finance Tracker.
"""

from datetime import datetime


class Expense:
    """
    Represents a single expense.
    """

    VALID_CATEGORIES = [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Entertainment",
        "Health",
        "Education",
        "Travel",
        "Other"
    ]

    def __init__(self, date, amount, category, description):
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.category = self.validate_category(category)
        self.description = self.validate_description(description)

    @staticmethod
    def validate_date(date):
        """
        Validate date format (YYYY-MM-DD)
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    @staticmethod
    def validate_amount(amount):
        """
        Validate expense amount.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
            return round(amount, 2)
        except:
            raise ValueError("Amount must be greater than 0.")

    @classmethod
    def validate_category(cls, category):
        """
        Validate category.
        """
        category = category.strip().title()

        if category not in cls.VALID_CATEGORIES:
            raise ValueError(
                f"Invalid category.\nAvailable Categories:\n{', '.join(cls.VALID_CATEGORIES)}"
            )

        return category

    @staticmethod
    def validate_description(description):
        """
        Validate description.
        """
        description = description.strip()

        if description == "":
            raise ValueError("Description cannot be empty.")

        return description

    def to_dict(self):
        """
        Convert Expense object into dictionary.
        """

        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Expense object from dictionary.
        """

        return cls(
            data["date"],
            data["amount"],
            data["category"],
            data["description"]
        )

    def __str__(self):
        return (
            f"{self.date} | "
            f"₹{self.amount:.2f} | "
            f"{self.category} | "
            f"{self.description}"
        )

    def __repr__(self):
        return (
            f"Expense(date='{self.date}', "
            f"amount={self.amount}, "
            f"category='{self.category}', "
            f"description='{self.description}')"
        )