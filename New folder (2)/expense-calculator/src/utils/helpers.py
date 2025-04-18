def format_currency(amount):
    """Format the amount as a currency string."""
    return f"${amount:,.2f}"

def validate_expense(expense):
    """Validate that the expense is a positive number."""
    if not isinstance(expense, (int, float)) or expense < 0:
        raise ValueError("Expense must be a positive number.")