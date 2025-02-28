# Define class
class ExpenseRecorder:
    
    # initialize the dictionary to store expenses
    def __init__(self):
        self.expenses = {}
                
        # Add a new expense
    def add_expense(self, date, category, amount, description):        
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append({
            'category': category,
            'amount': amount,
            'description': description
        })
        print(f"Expense added for {date}")

    # View all expenses or expenses for a specific date
    def view_expenses(self, date=None):        
        if date:
            if date in self.expenses:
                print(f"Expenses for {date}:")
                for expense in self.expenses[date]:
                    print(f"Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
            else:
                print(f"No expenses found for {date}")
        else:
            print("All Expenses:")
            for date, expenses in self.expenses.items():
                print(f"{date}:")
                for expense in expenses:
                    print(f"Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

    # Delete an expense for a specific date and category
    def delete_expense(self, date, category):        
        if date in self.expenses:
            self.expenses[date] = [expense for expense in self.expenses[date] if expense['category'] != category]
            print(f"Expense deleted for {date} and category {category}")
        else:
            print(f"No expenses found for {date}")

# Define main functon
def main():
    recorder = ExpenseRecorder()

   # Add looping statements
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            recorder.add_expense(date, category, amount, description)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD) or leave blank for all expenses: ")
            if date:
                recorder.view_expenses(date)
            else:
                recorder.view_expenses()
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            recorder.delete_expense(date, category)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main() # End of program.