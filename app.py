# Function to display welcome message
def display_welcome_message():
    print("Welcome to the Expense Tracker App!")

# Function to log an expense
def log_expense():
    # Prompt user for expense details
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category (Food/Transport/Entertainment): ").capitalize()
    description = input("Enter a description of the expense: ")

    # Validate inputs
    while amount <= 0:
        print("Please enter a positive number for the amount.")
        amount = float(input("Enter the expense amount: "))
    
    valid_categories = ["Food", "Transport", "Entertainment"]
    while category not in valid_categories:
        print("Please enter a valid category (Food, Transport, Entertainment).")
        category = input("Enter the expense category: ").capitalize()

    # Store expense
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)

# Function to display summary
def display_summary():
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal amount spent: ${total_spent:.2f}\n")

    categories = {}
    for expense in expenses:
        categories[expense['category']] = categories.get(expense['category'], 0) + expense['amount']

    print("Spending by category:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")

    print("\nAll expenses:")
    for expense in expenses:
        print(f"Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")

# Main program
if __name__ == "__main__":
    expenses = []

    display_welcome_message()

    while True:
        log_expense()

        choice = input("\nDo you want to log another expense? (yes/no): ").lower()
        if choice != "yes":
            break

    display_summary()
    print("\nThank you for using the Expense Tracker App!")

