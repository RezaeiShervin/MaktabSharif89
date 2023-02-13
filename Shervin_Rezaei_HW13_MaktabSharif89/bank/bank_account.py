class BankAccount:
    def __init__(self, title, balance):
        self.balance = balance
        self.title = title

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        assert self.balance > amount, "Insufficient Funds"
        self.balance -= amount

    def display_account_info(self, name):
        assert (self.balance - 1) > 0 , "Insufficient Funds"
        self.balance -= 1
        return f"User:{name}'s {self.title} and account balance is ${round(self.balance,2)}.\nCharging 1$ for taking balance!"


