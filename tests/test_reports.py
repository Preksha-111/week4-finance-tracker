"""
Tests for Reports
"""

import unittest

from finance_tracker.expense import Expense
from finance_tracker.reports import Reports


class TestReports(unittest.TestCase):


    def setUp(self):

        self.expenses = [

            Expense(
                "2026-08-01",
                500,
                "Food",
                "Dinner"
            ),

            Expense(
                "2026-08-02",
                1000,
                "Travel",
                "Taxi"
            )

        ]



    def test_category_report(self):

        report = Reports.category_report(
            self.expenses
        )


        self.assertEqual(
            report["Food"],
            500
        )


        self.assertEqual(
            report["Travel"],
            1000
        )



    def test_statistics(self):

        stats = Reports.statistics(
            self.expenses
        )


        self.assertEqual(
            stats["Total Expenses"],
            2
        )


if __name__ == "__main__":

    unittest.main()

    