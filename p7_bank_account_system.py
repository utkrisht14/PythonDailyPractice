class BankAccount:
    def __init__(self, account_holder_name, starting_balance):
        self.account_holder_name = account_holder_name
        self.balance = starting_balance

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Updated balance: {self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Updated balance: {self.balance}")

    def display_balance(self):
        print(f"{self.account_holder_name}'s balance: {self.balance}")

    def show_menu(self):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.display_balance()
            elif choice == "4":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


# Run program
my_bank_account = BankAccount("John Doe", 1000)
my_bank_account.show_menu()