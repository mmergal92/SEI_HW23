#BANK HOMEWORK
# Bank accounts should be created with the type of account (like "savings" or "checking").
# Each account should keep track of its current balance which should start at 0.
# Each account should have access to a deposit and a withdrawal method.
# The withdraw should return the amount withdrawn
# Deposit should return the new account balance after depositing
# Create a checking account and a savings account. Withdraw money from the savings account and deposit that amount into the checking account.
# Bonuses:
# Prevent withdrawing money if the balance will go negative.
# Start each account with an additional overdraft_fees property that starts at 0. If a call to withdraw ends with the balance below zero then overdraft_fees should be incremented by 20. You should also prevent the user from going below a balance of -100, including the overdraft fees.
# 
# Create a base BankAccount class
# Bank accounts keep track of their current balance
# Bank accounts have a deposit method - returns the balance of the account after adding
# Bank accounts have a withdraw method the deposited amount - returns the amount of money that was successfully withdrawn.
# Bank accounts return False if someone tries to deposit or withdraw a negative amount.
# Bank accounts are created with a default interest rate of 2%
# Bank accounts have a accumulate_interest method that sets the balance equal to the balance plus the balance times the interest rate
# accumulate_interest returns the balance of the account after calculating the accumulated interest

class BankAccount:
    def __init__(self, account_type, starting_balance):
        self.type = account_type
        self.balance = starting_balance
        self.overdraft_fees = 0
    def withdraw(self, amount):
        net_balance = self.balance - amount - self.overdraft_fees
        self.balance -= amount if net_balance >= -100 else 0
        if net_balance < -100:
            print("This is hitting the insufficient funds")
            return 'Insufficient Funds'
        if self.balance < 0:
            self.overdraft_fees += 20
        if amount <0:
            return False
        print(f"The amount is {amount}")
        print(f"The balance is {self.balance}")
        return amount
    def deposit(self, amount):
        self.balance += amount
        if amount <0:
            return False
        print(f"The balance is {self.balance} in your {self.type} account")
        return self.balance
    def accumulate_interest(self):
        self.balance = self.balance * 1.02
        print(f"The balance is {self.balance} in your {self.type} account")
        return self.balance
    def __str__(self):
        print(f"{self.type} has {self.balance}")
        return self.type 
chase = BankAccount("checking", 500)
# chase.deposit(500)
# print(chase.accumulate_interest())
# print(str(chase))

# Create a ChildrensAccount class
# Children's bank accounts have an interest rate of Zero.
# Every time accumulate_interest is executed on a Child's account the account always gets $10 added to the balance.

class childAccount(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
        self.overdraft_fees = 0
    def accumulate_interest(self):
        self.balance = self.balance + 10
        print(f"The balance is {self.balance} in your {self.type} account")
        return self.balance
# child = childAccount("checking", 500)
# child.deposit(30)
# print(child.accumulate_interest())

# Create an OverdraftAccount class
# An overdraft account penalizes customers for trying to draw too much money out of their account.
# Overdraft accounts are created with an overdraft_penalty property that defaults to $40.
# Customer's aren't allowed to withdraw more money than they have in their account. 
# If a customer tries to withdraw more than they have then the withdraw method returns False and their balance is deducted only by the amount of the overdraft_penalty.
# Overdraft accounts don't accumulate interest if their balance is below zero.

class OverdraftAccount(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
        self.overdraft_fees = 40
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= self.overdraft_fees
            return False
        super().withdraw(amount)
        print(f"The amount is {amount}")
        print(f"The balance is {self.balance}")
    def accumulate_interest(self):
        if self.balance > 0:
            self.balance = self.balance * 1.02
        print(f"The balance is {self.balance} in your {self.type} account")
        return self.balance
citibank = OverdraftAccount("checking", 20)
citibank.withdraw(15)
print(citibank.accumulate_interest())
print(str(citibank))

# Dunder Methods:
# When you print the bank account, make it so that it prints a well-formatted 
# blurb about the kind of account and its balance. 
# (ex. Savings Account: $50)
# Make it so that you can add the balances of two bank accounts by adding two instances of the class.
# Make it so that you can subtract, multiply, and divide the balances of two bank accounts by performing those mathematical operations on two instances of the class.
# Make it so that you can compare the balances of two bank accounts by using the greater 
# than, less than, and equals to operators in Python on two instances of the class.

class Dunder(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
    
    def __add__(self, other_accounts):
        combined_balance = self.balance + other_accounts.balance
        return Dunder(self.type, combined_balance)
    
    def __sub__(self, other_accounts):
        combined_balance = self.balance - other_accounts.balance
        return Dunder(self.type, combined_balance)

    def __mul__(self, other_accounts):
        combined_balance = self.balance * other_accounts.balance
        return Dunder(self.type, combined_balance)

    def __truediv__(self, other_accounts):
        combined_balance = self.balance / other_accounts.balance
        return Dunder(self.type, combined_balance)
    
    def __eq__(self, other_accounts):
        return self.balance == other_accounts.balance

    def __lt__(self, other_accounts):
        return self.balance < other_accounts.balance

    def __gt__(self, other_accounts):
        return self.balance > other_accounts.balance

account1 = Dunder("checking", 80)
account2 = Dunder("checking", 90)
account3 = Dunder("checking", 10)
print(account2 + account1 + account3)
print(account1 - account2 - account3)
print(account1 * account2 * account3)
print(account1 / account2 / account3)
print(account1 < account2)
print(account1 > account2)
print(account1 == account2)

