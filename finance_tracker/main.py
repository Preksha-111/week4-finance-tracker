"""
main.py
Main application for Personal Finance Tracker.
"""

from .expense import Expense
from .expense_manager import ExpenseManager
from .file_handler import FileHandler
from .reports import Reports
from .utils import (
    title,
    line,
    pause,
    get_date,
    get_amount,
    get_category,
    get_description,
    get_index,
    yes_no
)


class FinanceTracker:

    def __init__(self):

        self.manager = ExpenseManager()

        self.file_handler = FileHandler()

        self.manager.expenses = self.file_handler.load_expenses()

        # ---------------------------------------
    # Add Expense
    # ---------------------------------------

    def add_expense(self):

        title("ADD EXPENSE")

        try:

            date = get_date()

            amount = get_amount()

            category = get_category()

            description = get_description()

            expense = Expense(
                date,
                amount,
                category,
                description
            )

            self.manager.add_expense(expense)

            print("\n✅ Expense Added Successfully.")

        except Exception as e:

            print("\n❌", e)

        pause()

            # ---------------------------------------
    # View Expenses
    # ---------------------------------------

    def view_expenses(self):

        title("ALL EXPENSES")

        expenses = self.manager.get_all_expenses()

        if not expenses:

            print("No Expense Found.")

            pause()

            return

        line()

        print(
            f"{'No':<5}"
            f"{'Date':<15}"
            f"{'Amount':<12}"
            f"{'Category':<18}"
            f"Description"
        )

        line()

        for i, expense in enumerate(expenses, start=1):

            print(
                f"{i:<5}"
                f"{expense.date:<15}"
                f"₹{expense.amount:<11.2f}"
                f"{expense.category:<18}"
                f"{expense.description}"
            )

        line()

        print(f"\nTotal Expenses : {len(expenses)}")

        print(f"Total Amount   : ₹{self.manager.total_expense():.2f}")

        pause()

            # ---------------------------------------
    # Main Menu
    # ---------------------------------------

    def menu(self):

        while True:

            title("PERSONAL FINANCE TRACKER")

            print("1. Add Expense")

            print("2. View Expenses")

            print("3. Remove Expense")

            print("4. Search Expense")

            print("5. Filter Expense")

            print("6. Reports")

            print("7. Budget")

            print("8. Backup")

            print("9. Restore")

            print("10. Export CSV")

            print("11. Import CSV")

            print("12. Prediction")

            print("13. Exit")

            try:

                choice = int(input("\nEnter Choice : "))

            except:

                print("Invalid Choice.")

                pause()

                continue

            if choice == 1:
                self.add_expense()

            elif choice == 2:
                self.view_expenses()

            elif choice == 3:
                break

            elif choice == 4:
                break

            elif choice == 5:
                break

            elif choice == 6:
                break

            elif choice == 7:
                break

            elif choice == 8:
                break

            elif choice == 9:
                break

            elif choice == 10:
                break

            elif choice == 11:
                break

            elif choice == 12:
                break

            elif choice == 13:

                self.file_handler.save_expenses(
                    self.manager.expenses
                )

                print("\nThank You!")

                break

            else:

                print("Invalid Choice.")

                pause()


        # ---------------------------------------
    # Remove Expense
    # ---------------------------------------

    def remove_expense(self):

        title("REMOVE EXPENSE")

        expenses = self.manager.get_all_expenses()

        if not expenses:

            print("No expenses available.")

            pause()

            return

        self.view_expenses()

        try:

            index = get_index(len(expenses))

            removed = expenses[index]

            self.manager.remove_expense(index)

            print("\n✅ Expense Removed:")
            print(removed)

        except Exception as e:

            print("❌", e)

        pause()


    # ---------------------------------------
    # Search Expense
    # ---------------------------------------

    def search_expense(self):

        title("SEARCH EXPENSE")

        keyword = input(
            "Enter keyword to search: "
        ).strip()

        results = self.manager.search_description(
            keyword
        )

        if not results:

            print("No matching expense found.")

        else:

            for expense in results:

                print(expense)

        pause()


    # ---------------------------------------
    # Filter Expense
    # ---------------------------------------

    def filter_expense(self):

        title("FILTER EXPENSE")

        print("1. Filter By Category")

        print("2. Filter By Date")

        print("3. Filter By Month")


        try:

            choice = int(
                input("Choose option: ")
            )


        except:

            print("Invalid Choice.")

            pause()

            return


        results = []


        if choice == 1:

            category = get_category()

            results = self.manager.filter_category(
                category
            )


        elif choice == 2:

            date = get_date()

            results = self.manager.filter_date(
                date
            )


        elif choice == 3:

            month = input(
                "Enter Month (YYYY-MM): "
            )

            results = self.manager.filter_month(
                month
            )


        else:

            print("Invalid Option.")

            pause()

            return



        if not results:

            print("No expenses found.")


        else:

            print("\nFiltered Expenses:\n")

            for expense in results:

                print(expense)


        pause()


    # ---------------------------------------
    # Reports
    # ---------------------------------------

    def reports(self):

        title("EXPENSE REPORTS")


        expenses = self.manager.get_all_expenses()


        if not expenses:

            print("No data available.")

            pause()

            return


        print("1. Statistics")

        print("2. Category Report")

        print("3. Monthly Report")

        print("4. Complete Summary")


        try:

            choice = int(
                input("Choose option: ")
            )


        except:

            print("Invalid Choice.")

            pause()

            return



        if choice == 1:

            Reports.print_statistics(
                expenses
            )


        elif choice == 2:

            data = Reports.category_report(
                expenses
            )

            print("\nCategory Wise Expense\n")

            for key,value in data.items():

                print(
                    f"{key} : ₹{value:.2f}"
                )


        elif choice == 3:

            data = Reports.monthly_report(
                expenses
            )

            print("\nMonthly Expense\n")

            for key,value in data.items():

                print(
                    f"{key} : ₹{value:.2f}"
                )


        elif choice == 4:

            Reports.summary(
                expenses
            )


        else:

            print("Invalid Choice.")


        pause()

        # ---------------------------------------
    # Budget Management
    # ---------------------------------------

    def budget_menu(self):

        title("BUDGET MANAGEMENT")


        print("1. Set Budget")

        print("2. Check Budget Status")


        try:

            choice = int(
                input("Choose option: ")
            )


        except:

            print("Invalid Choice.")

            pause()

            return



        if choice == 1:

            try:

                amount = get_amount()

                self.manager.set_budget(
                    amount
                )

                print(
                    "\n✅ Budget Set Successfully."
                )


            except Exception as e:

                print(e)



        elif choice == 2:

            print(
                self.manager.budget_status()
            )


        else:

            print("Invalid Option.")


        pause()



    # ---------------------------------------
    # Create Backup
    # ---------------------------------------

    def backup_data(self):

        title("CREATE BACKUP")


        result = self.file_handler.create_backup()


        if result:

            print(
                "✅ Backup Created Successfully."
            )

        else:

            print(
                "❌ Backup Failed."
            )


        pause()



    # ---------------------------------------
    # Restore Backup
    # ---------------------------------------

    def restore_data(self):

        title("RESTORE BACKUP")


        confirm = yes_no(
            "Restore previous backup?"
        )


        if confirm:

            result = self.file_handler.restore_backup()


            if result:

                self.manager.expenses = (
                    self.file_handler.load_expenses()
                )

                print(
                    "✅ Backup Restored Successfully."
                )

            else:

                print(
                    "❌ Restore Failed."
                )


        pause()



    # ---------------------------------------
    # Export CSV
    # ---------------------------------------

    def export_csv(self):

        title("EXPORT CSV")


        result = self.file_handler.export_csv(
            self.manager.expenses
        )


        if result:

            print(
                "✅ CSV Exported Successfully."
            )

        else:

            print(
                "❌ Export Failed."
            )


        pause()



    # ---------------------------------------
    # Import CSV
    # ---------------------------------------

    def import_csv(self):

        title("IMPORT CSV")


        expenses = self.file_handler.import_csv()


        if expenses:


            for expense in expenses:

                self.manager.add_expense(
                    expense
                )


            self.file_handler.save_expenses(
                self.manager.expenses
            )


            print(
                "✅ CSV Imported Successfully."
            )


        else:

            print(
                "❌ No Data Found."
            )


        pause()



    # ---------------------------------------
    # Expense Prediction
    # ---------------------------------------

    def prediction(self):

        title("EXPENSE PREDICTION")


        predicted = (
            self.manager.predict_next_month()
        )


        print(
            f"Predicted Next Month Expense: ₹{predicted:.2f}"
        )


        pause()

        # ---------------------------------------
    # Save Data
    # ---------------------------------------

    def save_data(self):

        self.file_handler.save_expenses(
            self.manager.expenses
        )


    # ---------------------------------------
    # Updated Main Menu Runner
    # ---------------------------------------

    def run(self):

        while True:

            title("PERSONAL FINANCE TRACKER")


            print("1.  Add Expense")

            print("2.  View Expenses")

            print("3.  Remove Expense")

            print("4.  Search Expense")

            print("5.  Filter Expense")

            print("6.  Reports")

            print("7.  Budget Management")

            print("8.  Create Backup")

            print("9.  Restore Backup")

            print("10. Export CSV")

            print("11. Import CSV")

            print("12. Expense Prediction")

            print("13. Exit")


            try:

                choice = int(
                    input("\nEnter Choice : ")
                )


            except:

                print(
                    "Please enter number only."
                )

                pause()

                continue



            if choice == 1:

                self.add_expense()



            elif choice == 2:

                self.view_expenses()



            elif choice == 3:

                self.remove_expense()



            elif choice == 4:

                self.search_expense()



            elif choice == 5:

                self.filter_expense()



            elif choice == 6:

                self.reports()



            elif choice == 7:

                self.budget_menu()



            elif choice == 8:

                self.backup_data()



            elif choice == 9:

                self.restore_data()



            elif choice == 10:

                self.export_csv()



            elif choice == 11:

                self.import_csv()



            elif choice == 12:

                self.prediction()



            elif choice == 13:

                self.save_data()

                print(
                    "\n✅ Data Saved Successfully."
                )

                print(
                    "Thank You For Using Finance Tracker!"
                )

                break



            else:

                print(
                    "Invalid Option."
                )

                pause()



# ---------------------------------------
# Application Start Function
# ---------------------------------------

def main():

    app = FinanceTracker()

    app.run()



if __name__ == "__main__":

    main()

    