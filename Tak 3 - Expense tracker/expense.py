import json
from datetime import datetime


DATA_FILE = "expenses.json"


def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file)


def add_expense(amount, description, category):
    expenses = load_expenses()
    date = datetime.now().strftime("%Y-%m-%d")
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({"amount": amount, "description": description, "category": category})
    save_expenses(expenses)
    print("Expense added successfully!")


def get_monthly_summary():
    expenses = load_expenses()
    monthly_summary = {}
    for date, daily_expenses in expenses.items():
        month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += sum(expense["amount"] for expense in daily_expenses)
    return monthly_summary


def get_category_expenditure():
    expenses = load_expenses()
    category_expenditure = {}
    for daily_expenses in expenses.values():
        for expense in daily_expenses:
            if expense["category"] not in category_expenditure:
                category_expenditure[expense["category"]] = 0
            category_expenditure[expense["category"]] += expense["amount"]
    return category_expenditure


def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount spent: "))
            description = input("Enter brief description: ")
            category = input("Enter expense category: ")
            add_expense(amount, description, category)
        elif choice == "2":
            monthly_summary = get_monthly_summary()
            print("\nMonthly Summary:")
            for month, total_amount in monthly_summary.items():
                print(f"{month}: ${total_amount:.2f}")
        elif choice == "3":
            category_expenditure = get_category_expenditure()
            print("\nCategory-wise Expenditure:")
            for category, total_amount in category_expenditure.items():
                print(f"{category}: ${total_amount:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()