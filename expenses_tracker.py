'''import os
from datetime import datetime

#Creating the balance.txt file            
BALANCE_FILE = "balance.txt"
#adding some starting balance & checking if the file exists
if not os.path.exists(BALANCE_FILE):
    with open(BALANCE_FILE, "w") as f:
        f.write("100")   
    

def check_balance():
    with open(BALANCE_FILE, 'r') as file:
       balance = float(file.read().strip())
       print(f"Welcome! Your initial balance is: ${balance:.2f}")

#asking user if they want to add money to their balance
    answer = input("Do you wish to add money to your balance?(Y/N): ").strip().lower()
    if answer == "y":
        amount = float(input("Enter the amount you want to add: "))
        try:
            amount = float(amount)
            if amount >0:
                print("Amount updated successfully!")
            else:
                print("Enter a positive amount!")

#Update balance in balance.txt file
            new_balance = balance + amount 
            with open(BALANCE_FILE, "w") as f:
                f.write(str(new_balance))
            print(f"Balance updated successfully! This is your new balance: {new_balance:.2f}") 

        except:
            print("Enter a valid Input!!")
    elif answer == "n":
        print("No changes made to your initial balance.")
    else:
        print("Enter a valid input!")

today = datetime.today().strftime("%Y-%M-%D")
EXPENSES_FILE = f"expense_{today}.txt"
#checking if the file exists
if not os.path.exists(EXPENSES_FILE):
    open(EXPENSES_FILE, "w").close()
 
    print(f"New expense file has been created for {today}") 

#viewing your expenses
def view_expenses():
    print("""
          ================================================
          Your expense for {today} is:
          ================================================
          """)
    try:
        with open(EXPENSES_FILE, 'r') as expenses:
            lines = expenses.read()
        if lines.strip() == "":
            print("No expenses yet.")
        else: 
            print(lines)
    except:
        print("No recorded expenses at the moment!")
        print()

#Adding a new expense
def add_expense():
    try:
        with open(BALANCE_FILE, 'r') as file:
            current_balance= float(file.read().strip())
    except:
        current_balance = 0
    print(f"Your available balance is ${current_balance}")

    try:
        expense = float(input("How much do you wish to spend? $"))
        if expense <= 0:
            print("Enter a positive amount!")
            return
        if expense > current_balance:
            print("Insufficient Funds!!!")
            return
    except:
        print("Enter a valid number.")
        return
    
    Product = input("What did you buy? ")

    #Saving the expenses after adding them
    with open(EXPENSES_FILE, "a") as f:
        f.write(f"{expense} - {Product}")
                
    #updating balance after an expense
    new_balance = current_balance - expense
    with open(BALANCE_FILE, "w") as f:
        f.write(str(new_balance))

        print(f"Balance updated successfully! This is your new balance: {new_balance}") 

def main():
    print("Welcome to the Personal Expenses Tracker!")
    
    while True:
        print("")
        print("""================================================
                     MAIN MENU
================================================
        1. Check Your Remaining Balance
        2. View Your Expenses
        3. Add New Expense
        4. Exit
            """)
        
        choice = input("Enter your option to proceed: ").strip()
        try:
            choice=int(choice)
        except:
            print("Enter a valid input")
            continue
        
        if choice == 1:
            check_balance()      
        elif choice == 2:
            view_expenses()      
        elif choice == 3:
            add_expense()        
        elif choice == 4:
            print("Exiting and Saving data...") 
            break  
        else:
            print("Invalid option. Please choose 1-4: ")

main()'''

import os
from datetime import datetime

#creating balance.txt file and adding some initial amount
BALANCE_FILE = "balance.txt"


if not os.path.exists(BALANCE_FILE):
    with open(BALANCE_FILE, "w") as f:
        f.write("100.0")
elif os.path.getsize(BALANCE_FILE) == 0:  
    with open(BALANCE_FILE, "w") as f:
        f.write("100.0")


# Helper function
def get_expenses_file(date_str):
    return f"expenses_{date_str}.txt"



def read_balance():
    try:
        with open(BALANCE_FILE, 'r') as file:
            content = file.read().strip()
            if content == "":
                raise ValueError
            return float(content)
    except:
        print("Warning: Resetting to $100.0")
        with open(BALANCE_FILE, "w") as f:
            f.write("100.0")
        return 100.0


def write_balance(amount):
    with open(BALANCE_FILE, "w") as f:
        f.write(f"{amount:.2f}")



def check_balance():
    balance = read_balance()
    print(f"Welcome! Your current balance is: ${balance:.2f}")

    answer = input("\nDo you wish to add money to your balance? (Y/N): ").strip().lower()
    if answer == "y":
        try:
            amount = float(input("Enter the amount you want to add: $"))
            if amount > 0:
                new_balance = balance + amount
                write_balance(new_balance)
                print(f"Amount added successfully!")
                print(f"New balance: ${new_balance:.2f}\n")
            else:
                print("Please enter a positive amount!")
        except:
            print("Invalid input! Please enter a number.")
    else:
        print("No changes made.\n")



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
            print("Invalid date format! Use YYYY-MM-DD (e.g. 2025-11-19)")

    filename = get_expenses_file(date_str)

    print(f"\n{'='*50}")
    print(f"     EXPENSES FOR {date_str}")
    print(f"{'='*50}")

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No expenses recorded on this date.\n")
        return

    with open(filename, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        print(f"{i+1}. {line.strip()}")
    print()


def add_expense():
    current_balance = read_balance()
    print(f"Your available balance is: ${current_balance:.2f}\n")

    # Get amount
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

    # Get item
    product = input("What did you buy? ").strip()
    if not product:
        product = "No description"

    # Get date
    while True:
        date_input = input("\nEnter date of expense (YYYY-MM-DD) or press Enter for today: ").strip()
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
            print("Invalid date! Please use YYYY-MM-DD format.")

    # Save expense
    filename = get_expenses_file(date_str)
    with open(filename, "a") as f:
        f.write(f"${expense:.2f} - {product}\n")

    # Update balance
    new_balance = current_balance - expense
    write_balance(new_balance)

    print(f"\nExpense successfully added on {date_str}!")
    print(f"New balance: ${new_balance:.2f}\n")



def main():
    print("Welcome to the Personal Expenses Tracker!\n")

    while True:
        print("""===============================
               MAIN MENU
===============================
        1. Check Your Remaining Balance
        2. View Expenses (by date)
        3. Add New Expense (any date!)
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
            print("Thank you for using Expenses Tracker! Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1-4.\n")


main()