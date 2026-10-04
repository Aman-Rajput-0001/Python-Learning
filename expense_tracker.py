from datetime import date

# Defining lists to store values
expense_db = []
catogory_db = []
date_db = []

total = 0

print("-----------------------------------------------------------------------------------------------")
print("                                Expense Tracker                                                ")
print("-----------------------------------------------------------------------------------------------")

print("""Enter Your Choice
Enter 1 for Create New Expense
Enter 2 for Showing Total Spending
Enter 3 for Showing Category Wise Spending
Enter 4 for Highest Expense
Enter 5 for Today's Expense
""")

while True:
    user_input = int(input("Enter your choice: "))

    # Create new expense
    if user_input == 1:
        expense = int(input("Enter your spent amount: "))
        catogory = input("Enter your category for spending: ")

        expense_db.append(expense)
        catogory_db.append(catogory)
        date_db.append(date.today())

        print("Expense added successfully!")

    # Total spending
    elif user_input == 2:
        total = 0

        for i in expense_db:
            total = total + i

        print("Your Total Expense:", total)

    # Category-wise spending
    elif user_input == 3:
        catogory_total = {}

        for catogory, expense in zip(catogory_db, expense_db):

            if catogory in catogory_total:
                catogory_total[catogory] += expense
            else:
                catogory_total[catogory] = expense

        print("Category Wise Spending:")
        print(catogory_total)

    # Highest expense
    elif user_input == 4:

        if expense_db:
            print("Highest Expense:", max(expense_db))
        else:
            print("No expenses recorded.")

    # Today's expense
    elif user_input == 5:

        today_total = 0

        for today_expense, today_date in zip(expense_db, date_db):

            if today_date == date.today():
                today_total = today_total + today_expense

        print("Today's Total Expense:", today_total)

    # Invalid choice
    else:
        print("Invalid choice. Please enter 1-5.")


         



