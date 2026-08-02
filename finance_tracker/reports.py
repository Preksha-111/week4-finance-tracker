"""
reports.py
Generates reports and text-based visualizations.
"""

from collections import defaultdict


class Reports:

    @staticmethod
    def monthly_report(expenses):

        report = defaultdict(float)

        for expense in expenses:
            month = expense.date[:7]
            report[month] += expense.amount

        return dict(report)

    @staticmethod
    def category_report(expenses):

        report = defaultdict(float)

        for expense in expenses:
            report[expense.category] += expense.amount

        return dict(report)

    @staticmethod
    def statistics(expenses):

        if not expenses:
            return {
                "Total Expenses": 0,
                "Total Amount": 0,
                "Average": 0,
                "Highest": 0,
                "Lowest": 0
            }

        amounts = [expense.amount for expense in expenses]

        return {
            "Total Expenses": len(expenses),
            "Total Amount": round(sum(amounts), 2),
            "Average": round(sum(amounts) / len(amounts), 2),
            "Highest": max(amounts),
            "Lowest": min(amounts)
        }

    @staticmethod
    def expense_trend(expenses):

        report = defaultdict(float)

        for expense in expenses:
            report[expense.date] += expense.amount

        return dict(sorted(report.items()))

    @staticmethod
    def category_bar_chart(expenses):

        report = Reports.category_report(expenses)

        print("\n========== CATEGORY EXPENSES ==========\n")

        if not report:
            print("No expenses available.")
            return

        highest = max(report.values())

        scale = 40 / highest if highest else 1

        for category, amount in report.items():

            bars = "█" * int(amount * scale)

            print(f"{category:<15} ₹{amount:>8.2f}  {bars}")

    @staticmethod
    def monthly_bar_chart(expenses):

        report = Reports.monthly_report(expenses)

        print("\n========== MONTHLY REPORT ==========\n")

        if not report:
            print("No expenses available.")
            return

        highest = max(report.values())

        scale = 40 / highest if highest else 1

        for month, amount in sorted(report.items()):

            bars = "█" * int(amount * scale)

            print(f"{month:<10} ₹{amount:>8.2f}  {bars}")

    @staticmethod
    def print_statistics(expenses):

        stats = Reports.statistics(expenses)

        print("\n========== STATISTICS ==========\n")

        for key, value in stats.items():

            if isinstance(value, float):
                print(f"{key:<20}: ₹{value:.2f}")
            else:
                print(f"{key:<20}: {value}")

    @staticmethod
    def summary(expenses):

        Reports.print_statistics(expenses)

        print()

        Reports.category_bar_chart(expenses)

        print()

        Reports.monthly_bar_chart(expenses)


        