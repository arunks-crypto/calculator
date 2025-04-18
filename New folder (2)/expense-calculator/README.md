# Expense Calculator

This is a simple expense calculator application that allows users to manage their expenses efficiently. 

## Features

- Add expenses
- Remove expenses
- Calculate total expenses
- Format currency for better readability
- Validate expense entries

## Project Structure

```
expense-calculator/
├── src/
│   ├── main.py               # Entry point of the application
│   ├── calculator/            # Contains the expense calculator logic
│   │   ├── __init__.py       # Package initialization
│   │   └── expense_calculator.py  # ExpenseCalculator class
│   └── utils/                # Contains utility functions
│       ├── __init__.py       # Package initialization
│       └── helpers.py        # Utility functions for formatting and validation
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files and directories to ignore in version control
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd expense-calculator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the expense calculator, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to add, remove, and calculate your expenses.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.