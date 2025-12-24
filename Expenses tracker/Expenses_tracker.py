import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Rent, etc): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print(" Expense added successfully!\n")

def view_expenses():
    print("\n All Expenses:\n")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            summary[category] = summary.get(category, 0) + amount

    print("\n Category-wise Summary:")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total}")

def menu():
    while True:
        print("\n==== Smart Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("👋 Exiting... Bye!")
            break
        else:
            print("Invalid choice!")

init_file()
menu()


