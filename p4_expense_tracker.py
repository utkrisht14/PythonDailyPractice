expenses = {}

def add_expense(expenses: dict):
    num_input = int(input("How many expenses you want to enter: "))
    for i in range(num_input):
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expenses[expense_name] = expense_amount


def view_expenses(expenses: dict):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for k, v in expenses.items():
        print(f"{k} = {v}")


def total_expenses(expenses: dict):
    total = 0
    for v in expenses.values():
        total += v
    return total


def show_menu():
    while True:
        customer_input = int(input(
            "\n1. Add Expense\n"
            "2. View Expenses\n"
            "3. Show Total\n"
            "4. Exit\n"
            "Enter your choice: "
        ))

        if customer_input == 1:
            add_expense(expenses)
        elif customer_input == 2:
            view_expenses(expenses)
        elif customer_input == 3:
            print("Total Expenses:", total_expenses(expenses))
        elif customer_input == 4:
            print("Thank you for using the expense tracker.")
            break
        else:
            print("Invalid input. Please try again.")


# Run program
show_menu()