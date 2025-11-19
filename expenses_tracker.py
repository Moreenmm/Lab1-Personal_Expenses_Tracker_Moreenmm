import os
from datetime import date

def main():
    print("Welcome to the Personal Expenses Tracker!")
    
    while True:
        print("")
        print("""================================================
                           MAIN MENU
            ===================================================
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
            
BALANCE_FILE = "balance.txt"
#adding some starting balance & checking if the file exists
if not os.path.exists(BALANCE_FILE):
    with open(BALANCE_FILE, "w") as f:
        f.write("100")   
    print("Welcome! Your initial balance is 100.")

def check_balance():
    with open(BALANCE_FILE, 'r') as file:
       balance = float(file.read().strip())

#asking user if they want to add money to their balance
    answer = input("Do you wish to add money to your balance?(Y/N): ").strip().lower()
    if answer == "y":
        amount = input("Enter the amount you want to add: ")
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
            print(f"Balance updated successfully! This is your new balance: {new_balance}") 

        except:
            print("Enter a valid Input!!")
    elif answer == "n":
        print("No changes made.")
    else:
        print("Enter a valid input: ")

today = date.today()
EXPENSES_FILE = f"expense_{today}.txt"
#checking if the file exists
if not os.path.exists(EXPENSES_FILE):
    with open(EXPENSES_FILE, "w") as f:
        f.write("") 
        print(f"New expense file has been created for {today}") 

#viewing your expenses
def view_expenses():
    print("""
          ================================================
          Your expense for {today}:
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

main()