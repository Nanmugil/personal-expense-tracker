import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Date", "Category", "Amount", "Description"]
            )

def add_expense():
    print("\n--- Add New Expense ---")

    expense_date = input(
        "Enter date (YYYY-MM-DD) or press Enter for today: "
    ).strip()

    if expense_date == "":
        expense_date = date.today().isoformat()
    else:
        try:
            date.fromisoformat(expense_date)
        except ValueError:
            print("Invalid date format.")
            return

    category = input("Enter category: ").strip().title()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    description = input("Enter description: ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            expense_date, category, f"{amount:.2f}", description
        ])

    print("Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("-" * 65)
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 65)

    for expense in expenses:
        print(
            f"{expense['Date']:<12} "
            f"{expense['Category']:<15} "
            f"{float(expense['Amount']):>10.2f}  "
            f"{expense['Description']}"
        )

    print("-" * 65)

def filter_expenses():
    category = input(
        "Enter category to filter: "
    ).strip().casefold()

    if not category:
        print("Category cannot be empty.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = [
            expense for expense in reader
            if expense["Category"].casefold() == category
        ]

    if not expenses:
        print("No expenses found for this category.")
        return

    print(f"\n--- {category.title()} Expenses ---")

    for expense in expenses:
        print(
            f"{expense['Date']} | "
            f"{expense['Category']} | "
            f"Rs. {float(expense['Amount']):.2f} | "
            f"{expense['Description']}"
        )

def category_summary():
    totals = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            totals[category] = totals.get(category, 0) + amount

    if not totals:
        print("No expenses available for summary.")
        return

    print("\n--- Category Summary ---")

    for category, total in sorted(totals.items()):
        print(f"{category:<15} Rs. {total:.2f}")

    grand_total = sum(totals.values())
    print("-" * 30)
    print(f"{'Total Spending':<15} Rs. {grand_total:.2f}")

def main():
    create_file()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
