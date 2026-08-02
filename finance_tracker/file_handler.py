"""
file_handler.py
Handles JSON, CSV, Backup and Restore operations.
"""

import os
import json
import csv
import shutil

from .expense import Expense


class FileHandler:

    def __init__(self):

        self.data_file = "data/expenses.json"
        self.backup_folder = "data/backup"
        self.export_folder = "data/exports"

        if not os.path.isdir(self.backup_folder):
            os.makedirs(self.backup_folder, exist_ok=True)

        if not os.path.isdir(self.export_folder):
            os.makedirs(self.export_folder, exist_ok=True)

    # --------------------------------
    # Save JSON
    # --------------------------------

    def save_expenses(self, expenses):

        try:

            data = [expense.to_dict() for expense in expenses]

            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return True

        except Exception as e:
            print("Error Saving File:", e)
            return False

    # --------------------------------
    # Load JSON
    # --------------------------------

    def load_expenses(self):

        if not os.path.exists(self.data_file):
            return []

        try:

            with open(self.data_file, "r", encoding="utf-8") as file:

                data = json.load(file)

            expenses = [
                Expense.from_dict(item)
                for item in data
            ]

            return expenses

        except Exception as e:

            print("Error Loading File:", e)
            return []

    # --------------------------------
    # Backup
    # --------------------------------

    def create_backup(self):

        try:

            backup_file = os.path.join(
                self.backup_folder,
                "expenses_backup.json"
            )

            shutil.copy(self.data_file, backup_file)

            return True

        except Exception as e:

            print("Backup Failed:", e)

            return False

    # --------------------------------
    # Restore Backup
    # --------------------------------

    def restore_backup(self):

        try:

            backup_file = os.path.join(
                self.backup_folder,
                "expenses_backup.json"
            )

            shutil.copy(
                backup_file,
                self.data_file
            )

            return True

        except Exception as e:

            print("Restore Failed:", e)

            return False

    # --------------------------------
    # Export CSV
    # --------------------------------

    def export_csv(self, expenses):

        try:

            csv_file = os.path.join(
                self.export_folder,
                "expenses.csv"
            )

            with open(csv_file,
                      "w",
                      newline="",
                      encoding="utf-8") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Date",
                    "Amount",
                    "Category",
                    "Description"
                ])

                for expense in expenses:

                    writer.writerow([
                        expense.date,
                        expense.amount,
                        expense.category,
                        expense.description
                    ])

            return True

        except Exception as e:

            print("CSV Export Failed:", e)

            return False

    # --------------------------------
    # Import CSV
    # --------------------------------

    def import_csv(self):

        csv_file = os.path.join(
            self.export_folder,
            "expenses.csv"
        )

        if not os.path.exists(csv_file):

            print("CSV file not found.")

            return []

        expenses = []

        try:

            with open(csv_file,
                      "r",
                      encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    expense = Expense(

                        row["Date"],

                        row["Amount"],

                        row["Category"],

                        row["Description"]

                    )

                    expenses.append(expense)

            return expenses

        except Exception as e:

            print("CSV Import Failed:", e)

            return []

    # --------------------------------
    # File Exists
    # --------------------------------

    def file_exists(self):

        return os.path.exists(self.data_file)

    # --------------------------------
    # Delete File
    # --------------------------------

    def delete_data_file(self):

        try:

            if os.path.exists(self.data_file):

                os.remove(self.data_file)

                return True

            return False

        except Exception as e:

            print(e)

            return False

        
