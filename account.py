class Account:
    def __init__(self):
        self.balance = 0
        print('Starting balance is: ', self.balance)

    def deposit(self, amount):
        self.balance += amount
        print('Account balance is: ', self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print('Account balance is: ', self.balance)



