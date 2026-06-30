from data_handling import expenses

def view_expenses():
    if len(expenses) == 0:
        print("\nNo Expenses Found.\n")
        return

    print("\n------ Expenses ------")

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print(f"Category    : {expense['category']}")
        print(f"Amount      : ₹{expense['amount']}")
        print(f"Description : {expense['description']}")