class Transaction:
    def __init__(self, transaction_id, amount, category):
        self.transaction_id = transaction_id
        self.amount = amount
        self.category = category

    def display_info(self):
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount}, Category: {self.category}"


class Deposit(Transaction):
    def __init__(self, transaction_id, amount, category, source):
        super().__init__(transaction_id, amount, category)
        self.source = source


class Withdrawal(Transaction):
    def __init__(self, purpose, transaction_id, amount, category):
        super().__init__(transaction_id, amount, category)
        self.purpose = purpose


class Transfer(Transaction):
    def __init__(self, transaction_id, amount, category,  receiver):
        super().__init__(transaction_id, amount, category)
        self.receiver = receiver


class Wallet:
    def __init__(self):
        self.transactions = []

    def __len__(self):
        return len(self.transactions)

    def add_transaction(self, transaction: Transaction):
        for current_id in self.transactions:
            if current_id == transaction.transaction_id:
                print("Transaction already exists.")
                return

        self.transactions.append(transaction)


    def view_transaction(self):
        if not self.transactions:
            print("No transactions available.")
            return

        for transaction in self.transactions:
            print(transaction.display_info())


    def search_by_attribute(self, attribute_name, value):
        for transaction in self.transactions:
            attr = getattr(transaction, attribute_name, None)
            if attr is not None and str(attr).lower() == str(value).lower():
                print(transaction.display_info())
                return


deposit = Deposit(1, 1000, "Salary", "Bank")
withdrawal = Withdrawal("Monthly rent", 500, "Housing", "Bank")
transfer = Transfer(2, 500, "Utilities", "Friend")

wallet = Wallet()
wallet.add_transaction(deposit)
wallet.add_transaction(withdrawal)
wallet.add_transaction(transfer)
wallet.view_transaction()
wallet.search_by_attribute("transaction_id", 2)


