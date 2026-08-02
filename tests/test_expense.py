"""
Tests for Expense class
"""

import unittest

from finance_tracker.expense import Expense


class TestExpense(unittest.TestCase):


    def test_create_expense(self):

        expense = Expense(
            "2026-08-02",
            500,
            "Food",
            "Lunch"
        )

        self.assertEqual(
            expense.amount,
            500
        )

        self.assertEqual(
            expense.category,
            "Food"
        )


    def test_invalid_amount(self):

        with self.assertRaises(ValueError):

            Expense(
                "2026-08-02",
                -100,
                "Food",
                "Test"
            )


    def test_invalid_date(self):

        with self.assertRaises(ValueError):

            Expense(
                "02-08-2026",
                100,
                "Food",
                "Test"
            )


if __name__ == "__main__":

    unittest.main()

    