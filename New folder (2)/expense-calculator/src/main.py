# filepath: expense-calculator/src/main.py

from calculator.expense_calculator import ExpenseCalculator

def main():
    calculator = ExpenseCalculator()
    
    while True:
        print("\nExpense Calculator")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Calculate Total")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            calculator.add_expense(amount, description)
            print(f"Added expense: {description} - ${amount:.2f}")
        
        elif choice == '2':
            description = input("Enter expense description to remove: ")
            calculator.remove_expense(description)
            print(f"Removed expense: {description}")
        
        elif choice == '3':
            total = calculator.calculate_total()
            print(f"Total expenses: ${total:.2f}")
        
        elif choice == '4':
            print("Exiting the Expense Calculator.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()