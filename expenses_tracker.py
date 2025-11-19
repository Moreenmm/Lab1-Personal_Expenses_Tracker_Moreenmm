import os
from datetime import datetime

BALANCE_FILE = "balance.txt"

# ----------------------------------------------------
# Create the balance file if it doesn't exist or is empty
# ----------------------------------------------------
if not os.path.exists(BALANCE_FILE) or os.path.getsize(BALANCE_FILE) == 0:
    with open(BALANCE_FILE, "w") as f:
        f.write("100.0")

# ----------------------------------------------------
# Helper function to get expense file name
# ----------------------------------------------------
def get_expenses_file(date_str):
    return f"expenses_{date_str}.txt"


# ----------------------------------------------------
# Read balance safely
# ----------------------------------------------------
def read_balance():
    try:
        with open(BALANCE_FILE, "r") as file:
            content = file.read().strip()
            if content == "":
                raise ValueError
            return float(content)
    except:
        print("Warning: Resetting balance to $100.0")
        write_balance(100.0)
        return 100.0


# ----------------------------------------------------
# Write new balance to file
# ----------------------------------------------------
def write_balance(amount):
    with open(BALANCE_FILE, "w") as f:
        f.write(f"{amount:.2f}")


# ----------------------------------------------------
# CHECK REMAINING BALANCE
# ----------------------------------------------------
def check_balance():
    balance = read_balance()
    print(f"\nYour current balance is: ${balance:.2f}")

    answer = input("Do you wish to add money? (Y/N): ").strip().lower()
    if answer == "y":
        try:
            amount = float(input("Enter amount to add: $"))
            if amount > 0:
                new_balance = balance + amount
                write_balance(new_balance)
                print(f"Amount successfully added!")
                print(f"New balance: ${new_balance:.2f}\n")
            else:
                print("Please enter a positive number.\n")
        except:
            print("Invalid input. Please enter a valid number.\n")
    else:
        print("No changes made.\n")


# ----------------------------------------------------
# VIEW EXPENSES
# ----------------------------------------------------
def view_expenses():
    while True:
        date_input = input("Enter date to view (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input == "":
            date_str = datetime.today().strftime("%Y-%m-%d")
            break
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date_str = date_input
            break
        except:
            print("Invalid date format! Use YYYY-MM-DD")

    filename = get_expenses_file(date_str)

    print("\n========================================")
    print(f"         EXPENSES FOR {date_str}")
    print("========================================")

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No expenses recorded on this date.\n")
        return

    with open(filename, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        print(f"{i+1}. {line.strip()}")
    print()


# ----------------------------------------------------
# ADD NEW EXPENSE
# ----------------------------------------------------
def add_expense():
    current_balance = read_balance()
    print(f"\nYour available balance is: ${current_balance:.2f}\n")

    # Get expense amount
    try:
        expense = float(input("How much did you spend? $"))
        if expense <= 0:
            print("Amount must be positive!")
            return
        if expense > current_balance:
            print("Insufficient funds!")
            return
    except:
        print("Please enter a valid number!")
        return

    # Get item name
    product = input("What did you buy? ").strip()
    if product == "":
        product = "No description"

    # Get date
    while True:
        date_input = input("Enter date of expense (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input == "":
            date_str = datetime.today().strftime("%Y-%m-%d")
            print(f"→ Using today: {date_str}")
            break
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date_str = date_input
            print(f"→ Date set: {date_str}")
            break
        except ValueError:
            print("Invalid date format!")

    # Determine next expense ID
    filename = get_expenses_file(date_str)
    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing = f.readlines()
        expense_id = len(existing) + 1
    else:
        expense_id = 1

    # Save expense
    with open(filename, "a") as f:
        timestamp = datetime.now().strftime("%H:%M:%S")
        f.write(f"ID {expense_id} | ${expense:.2f} | {product} | Time: {timestamp}\n")

    # Update balance
    new_balance = current_balance - expense
    write_balance(new_balance)

    print(f"\nExpense successfully added!")
    print(f"Recorded as ID {expense_id} on {date_str}")
    print(f"New balance on file: ${new_balance:.2f}\n")


# ----------------------------------------------------
# MAIN MENU SYSTEM
# ----------------------------------------------------
def main():
    print("Welcome to the Personal Expenses Tracker!\n")

    while True:
        print("""===============================
           MAIN MENU
===============================
1. Check Remaining Balance
2. View Expenses (by date)
3. Add New Expense
4. Exit
""")

        choice = input("Enter your option (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_expense()
        elif choice == "4":
            print("Thank you for using the Expenses Tracker! Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1-4.\n")


main()
