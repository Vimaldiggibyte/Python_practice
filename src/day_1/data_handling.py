expenses = []

def add_expense(expense):
    expenses.append(expense)


def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Expense Deleted Successfully.")
    else:
        print("Invalid Expense Number.")