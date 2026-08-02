"""
utils.py
Utility functions for Personal Finance Tracker.
"""

from datetime import datetime


def line():
    """Print separator line."""
    print("-" * 60)


def title(text):
    """Print formatted title."""
    line()
    print(text.center(60))
    line()


def pause():
    """Pause until user presses Enter."""
    input("\nPress Enter to continue...")


def get_date():
    """
    Get valid date from user.
    Format: YYYY-MM-DD
    """

    while True:

        date = input("Enter Date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("❌ Invalid Date Format.")


def get_amount():

    while True:

        value = input("Enter Amount: ₹").strip()

        try:

            value = float(value)

            if value <= 0:
                raise ValueError

            return round(value, 2)

        except:
            print("❌ Enter valid amount.")


def get_category():

    categories = [
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

    print()

    print("Available Categories")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    while True:

        value = input("\nChoose Category: ").strip()

        try:

            index = int(value)

            if 1 <= index <= len(categories):
                return categories[index - 1]

            print("Invalid Choice.")

        except:

            value = value.title()

            if value in categories:
                return value

            print("Invalid Category.")


def get_description():

    while True:

        description = input("Description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")


def get_index(max_size):

    while True:

        try:

            index = int(input("Enter Expense Number: "))

            if 1 <= index <= max_size:
                return index - 1

            print("Invalid Number.")

        except:

            print("Enter Integer Only.")


def yes_no(message):

    while True:

        ans = input(f"{message} (Y/N): ").strip().lower()

        if ans in ["y", "yes"]:
            return True

        if ans in ["n", "no"]:
            return False

        print("Please Enter Y or N.")


