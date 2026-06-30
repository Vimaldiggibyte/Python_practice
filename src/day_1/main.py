from data_handling import add_expense, delete_expense, expenses
from display import view_expenses
from calculation import total_expense, highest_expense


def get_expense():
    category = input("Enter the Category: ")
    amount = float(input("Enter the Amount: "))
    description = input("Enter the Description: ")

    return {
        "category": category,
        "amount": amount,
        "description": description
    }


def main():
    while True:
        print("\n========== Personal Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expense")
        print("5. Highest Expense")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            expense = get_expense()
            add_expense(expense)
            print("Expense Added Successfully.")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            if len(expenses) == 0:
                print("No Expenses Found.")
            else:
                view_expenses()
                try:
                    index = int(input("\nEnter Expense Number to Delete: ")) - 1
                    delete_expense(index)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            total_expense()

        elif choice == "5":
            highest_expense()

        elif choice == "6":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()