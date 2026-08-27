##################### Warm-Up #######################
# How many names/bindings will be in the Global frame
# when these lines are run?
class Example:
    x = 2
    y = 3
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def greeting(self):
        print("hello")
        
x = 1
z = 0

ex = Example(12, z)


class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds. See our FAQ'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    '''
    >>> ch = CheckingAccount('Tom')
    >>> ch.interest     # Lower interest rate for checking accounts
    0.01
    >>> ch.deposit(20)  # Deposits are the same
    20
    >>> ch.withdraw(5)  # Withdrawals incur a $1 fee
    14
    '''
    interest = .01
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    
