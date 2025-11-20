Personal expense tracker app
    1.An application that tracks expenses and also calculates your current balance from the amount you had initially. It also prompts one to add some money to top up the initial amount. In the expenses_tracker.py you get a menu with:
             1. Check the remaining balance
             2. View expenses
             3. Add expenses 
             4. Exit
    Once you run the python script it creates a balance.txt file and an expenses_{date}.txt file. The balance.txt file shows the initial balance and the expenses_{date}.txt shows all the added expenses with an id, name of the expense, date, and the amount spent on the expense.
    The script also shows the available balance before you add an expense to avoid going above your budget. It allows you to add the date of expenses to help you manage your finances responsibly.


     2. There's also an archive_expenses.sh where the expenses are moved to after adding them. You can also search for expenses using the date of the expenses.
    This shell script creates a directory named  archives and a archive_log.txt file where the expenses data in the expenses_{date}.txt is stored. The archives_log.txt file is inside the archives directory.
