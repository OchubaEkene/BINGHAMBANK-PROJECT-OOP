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

class ChildrenAccount(Account):
    def deposit(self, amount):
        self.balance += amount * 0.007
        super().deposit(amount)


    def withdraw(self, amount):
        print("No withdrawals are allowed for children account")

d = ChildrenAccount()
d.deposit(1000)
d.withdraw(10)


class CurrentAccount(Account):
    pass

d = CurrentAccount()
d.deposit(1000)



class SavingsAccount(Account):
    def deposit(self, amount):
            self.balance += amount * 0.005
            super().deposit(amount)

    def withdraw(self, amount):
        if amount <= 700000:
            super().withdraw(amount)
        else:
            print("You have reached your withdrawal limit")

d = SavingsAccount()
d.deposit(100000000)
