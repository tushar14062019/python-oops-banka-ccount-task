class Bank_Acc:
    total_Acc = 0

    def __init__(self, Acc_Owner, balance=0):
        if not Acc_Owner:
            raise ValueError("Enter the Name.")
        if not self.Valid_Amt(balance):
            raise ValueError("Initial balance is Invalid.")
        self.Acc_Owner = Acc_Owner
        self.balance = balance
        self.transactions = []
        Bank_Acc.total_Acc +=1
        print(f"Account is created for {self.Acc_Owner}.")

    def Deposite(self, amount):
        if self.Valid_Amt(amount):
            self.balance = self.balance+amount
            self.transactions.append(f"Deposited amount is ₹{amount}")
        else:
            print("The Deposited amount is Invalid.")

    def Withdrawal(self, amount):
        if not self.Valid_Amt(amount) or amount > 60000:
            print("Enter correct Amount.")
            return
        if self.balance - amount < 0:
            print("Insufficient Balance.")
            return
        
        self.balance -= (amount + 20)
        self.transactions.append(f"Withdrawal Amount ₹{amount} and ₹20 fee")

    def transfer(self, recipient, amount):
        if not isinstance(recipient, Bank_Acc):
            print("This recipient is invalid.")
            return
        if not self.Valid_Amt(amount):
            print("Enter Correct Amount for transfer.")
            return
        if self.balance - amount < 0:
            print("Insufficient Balance.")
            return
        
        self.balance -= amount
        recipient.balance += amount
        self.transactions.append(f"Transferred Amount is: ₹{amount} to {recipient.Acc_Owner}")
        recipient.transactions.append(f"Received Amount is: ₹{amount} from {self.Acc_Owner}")

    def check_balance(self):
        print(f"The balance of {self.Acc_Owner} is: ₹{self.balance}.")

    def Transcation_History(self):
        return self.transactions

    @classmethod
    def total_bank_Accounts(cls):
        return cls.total_Acc
    
    @staticmethod
    def Valid_Amt(amount):
        return isinstance(amount, (int, float)) and amount > 0 and amount <= 60000

Acc = Bank_Acc("Anuj Kadam", 60000)
Acc.Deposite(50025)
Acc.check_balance()
print("Transaction History for Anuj Kadam", Acc.Transcation_History())
print("Total bank Accounts:", Bank_Acc.total_bank_Accounts())
