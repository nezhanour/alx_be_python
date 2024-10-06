class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            return f"Insufficient funds."
        else:
            self.account_balance =- amount
            return self.account_balance
    
    
    def display_balance(self):
        print(self.account_balance) 