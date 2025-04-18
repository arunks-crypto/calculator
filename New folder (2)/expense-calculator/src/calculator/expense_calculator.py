class ExpenseCalculator:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description):
        if self.validate_expense(amount):
            self.expenses.append({'amount': amount, 'description': description})
        else:
            raise ValueError("Invalid expense amount")

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
        else:
            raise IndexError("Expense index out of range")

    def calculate_total(self):
        return sum(expense['amount'] for expense in self.expenses)

    @staticmethod
    def validate_expense(amount):
        return isinstance(amount, (int, float)) and amount > 0