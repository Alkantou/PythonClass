# For this challenge, create a bank account class that has two attributes:
#
# owner
# balance
# and two methods:
#
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make
# sure the account can't be overdrawn.


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount balance: ${self.balance}'


    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if wd_amt <= self.balance:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable')


account1 = Account('Alex', 100)
print(account1)

account1.withdraw(15)

print(account1.balance)