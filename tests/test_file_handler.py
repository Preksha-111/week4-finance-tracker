"""
Tests for File Handler
"""

import unittest
import os

from finance_tracker.expense import Expense
from finance_tracker.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):


    def setUp(self):

        self.handler = FileHandler()


    def test_save_file(self):

        expense = Expense(
            "2026-08-02",
            1000,
            "Travel",
            "Bus"
        )


        result = self.handler.save_expenses(
            [expense]
        )


        self.assertTrue(result)



    def test_load_file(self):

        expenses = self.handler.load_expenses()

        self.assertIsInstance(
            expenses,
            list
        )


if __name__ == "__main__":

    unittest.main()

    