
from data_handling import expenses



def total_expense():
    total = 0
    for exp in expenses:
        total += exp['amount']
    print("Total expense",total)



def highest_expense():
    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\nHighest Expense")
    print("Category :", highest["category"])
    print("Amount   :", highest["amount"])
    print("Description :", highest["description"])
