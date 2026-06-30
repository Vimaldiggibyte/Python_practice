def get_expense():
    category = input("Enter the Category: ")
    amount = int(input("Enter the amount: "))
    description = input("Enter the description: ")

    return {
        "category": category,
        "amount": amount,
        "description": description
    }