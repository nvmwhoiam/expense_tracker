# Python Expense Tracker

This Python program helps users track their daily expenses by allowing them to log expenses, categorize them, and view a summary of their spending.

## Features

- **Welcome Message:**

  - Displays a welcome message when the program starts.

- **Log Expense:**

  - Prompts the user to enter the expense amount, category, and description.
  - Validates input to ensure the amount is positive and the category is valid.
  - Stores the expense data using a list of dictionaries.

- **Display Summary:**

  - Shows the total amount spent.
  - Displays the total amount spent in each expense category.
  - Lists all logged expenses with their details.

- **Data Validation:**

  - Ensures that the user inputs a positive number for the expense amount.
  - Validates that the expense category belongs to a predefined list.

- **Thank You Message:**

  - Thanks the user for using the expense tracker when exiting the program.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/nvmwhoiam/expense_tracker.git
```

2. **Navigate into the project directory:**

```bash
cd expense_tracker
```

3. **Run the program:**

```bash
python app.py
```

## Usage

- Upon running the program, follow the prompts to log your expenses.
- Enter the expense amount, choose a category (Food, Transport, Entertainment), and describe the expense.
- Continue logging expenses until you decide to stop.
- The program will display a summary of your expenses when you finish logging.

## Example

Here's a quick example of how the program might look:

```text
Welcome to the Expense Tracker App!

Enter the expense amount: 25.50
Enter the expense category (Food/Transport/Entertainment): Food
Enter a description of the expense: Lunch at a restaurant

Do you want to log another expense? (yes/no): yes

Enter the expense amount: 15.00
Enter the expense category (Food/Transport/Entertainment): Transport
Enter a description of the expense: Taxi ride

Do you want to log another expense? (yes/no): no

Total amount spent: $40.50

Spending by category:
Food: $25.50
Transport: $15.00

All expenses:
Amount: $25.50, Category: Food, Description: Lunch at a restaurant
Amount: $15.00, Category: Transport, Description: Taxi ride

Thank you for using the Expense Tracker App!
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- nvmwhoiam
- GitHub: <a href="https://github.com/nvmwhoiam">Your GitHub Profile</a>
