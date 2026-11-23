import csv
import os
from datetime import date, datetime

FILE = "expenses.csv"
BUDGET_FILE = "budget.txt"


def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")
    description = input("Enter description: ")

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(
                ["Date", "Amount", "Category", "Description"]
            )

        writer.writerow(
            [date.today(), amount, category, description]
        )

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    with open(FILE, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)


def set_budget():
    budget = float(input("Enter your monthly budget: ₹"))

    with open(BUDGET_FILE, "w") as f:
        f.write(str(budget))

    print("Monthly budget saved successfully!")


def monthly_analysis():
    total = 0

    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    current_month = date.today().strftime("%Y-%m")

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Date"].startswith(current_month):
                total += float(row["Amount"])

    print("\n===== MONTHLY ANALYSIS =====")
    print("Total Monthly Expenses: ₹", total)

    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            budget = float(f.read())

        print("Monthly Budget: ₹", budget)
        print("Remaining Budget: ₹", budget - total)

        if total > budget:
            print("Warning! You have exceeded your budget.")


def category_analysis():
    categories = {}

    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            categories[category] = categories.get(category, 0) + amount

    print("\n===== CATEGORY ANALYSIS =====")

    for category, amount in categories.items():
        print(category, ": ₹", amount)


while True:

    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Budget Analysis")
    print("4. Set Monthly Budget")
    print("5. Category Analysis")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        monthly_analysis()

    elif choice == "4":
        set_budget()

    elif choice == "5":
        category_analysis()

    elif choice == "6":
        print("Thank you for using Smart Expense Tracker!")
        break

    else:
        print("Invalid choice!")