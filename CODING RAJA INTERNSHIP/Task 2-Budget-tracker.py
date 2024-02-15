import json

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, category, amount, transaction_type):
        transaction = {"category": category, "amount": amount, "type": transaction_type}
        self.transactions.append(transaction)
        print(f"{transaction_type.capitalize()} of {amount} in {category} added.")

    def calculate_budget(self):
        total_income = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "income")
        total_expenses = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "expense")
        remaining_budget = total_income - total_expenses
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Remaining Budget: {remaining_budget}")

    def analyze_expenses(self):
        expenses_by_category = {}
        for transaction in self.transactions:
            if transaction["type"] == "expense":
                category = transaction["category"]
                amount = transaction["amount"]
                expenses_by_category[category] = expenses_by_category.get(category, 0) + amount
        if expenses_by_category:
            print("Expenses by Category:")
            for category, amount in expenses_by_category.items():
                print(f"{category}: {amount}")
        else:
            print("No expenses recorded yet.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            print("File not found. Starting with an empty transaction list.")
            self.transactions = []
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty transaction list.")
            self.transactions = []

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.transactions, file)

def main():
    budget_tracker = BudgetTracker()
    budget_tracker.load_from_file("transactions.json")
    
    while True:
        print("\nOptions:")
        print("1. Add income")
        print("2. Add expense")
        print("3. Calculate budget")
        print("4. Analyze expenses")
        print("5. Save transactions to file")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter the income category: ")
            amount = float(input("Enter the income amount: "))
            budget_tracker.add_transaction(category, amount, "income")
        elif choice == '2':
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            budget_tracker.add_transaction(category, amount, "expense")
        elif choice == '3':
            budget_tracker.calculate_budget()
        elif choice == '4':
            budget_tracker.analyze_expenses()
        elif choice == '5':
            budget_tracker.save_to_file("transactions.json")
            print("Transactions saved to file.")
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
