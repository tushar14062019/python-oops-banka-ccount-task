class BankAccount:
    total_accounts = 0  # Class variable to track total accounts

    def __init__(self, account_holder, initial_balance=0):
        """Initialize a new bank account."""
        pass

    def deposit(self, amount):
        """Instance method to deposit money into the account."""
        pass

    def withdraw(self, amount):
        """Instance method to withdraw money, applying a transaction fee."""
        pass

    def transfer(self, recipient, amount):
        """Instance method to transfer money between two accounts."""
        pass

    def check_balance(self):
        """Instance method to check the current balance."""
        pass

    def get_transaction_history(self):
        """Instance method to return a list of all transactions."""
        pass

    @classmethod
    def total_bank_accounts(cls):
        """Class method to return the total number of accounts."""
        pass

    @staticmethod
    def validate_amount(amount):
        """Static method to check if an amount is valid (positive, within limits)."""
        pass
