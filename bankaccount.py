# class User:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f'Hi! My name is {self.name}')
# me = User('Maria')
# me.greet()

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
    def test_function(self):
        return ("test")
    def __str__(self):
        print(f"{self.type} has {self.balance}")
        return self.type 
chase = BankAccount("checking", 500)
print(chase.test_function())
# chase.deposit(500)
print(chase.accumulate_interest())
print(str(chase))

class childAccount(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
        self.overdraft_fees = 0
    def accumulate_interest(self):
        self.balance = self.balance + 10
        print(f"The balance is {self.balance} in your {self.type} account")
        return self.balance
    def test_function(self):
        return ("test")
child = childAccount("checking", 500)
print(child.accumulate_interest())
print(child.test_function())


# class Fancy(BankAccount):
#     def __init__(self, account_type, starting_balance):
#         super().__init__(account_type)
#         super().__init__(starting_balance)
#         self.time = 0
#     def accumulate_interest(self, amount, time):
#         self.balance += amount + (amount(1 + 0.02*time))
#         return self.balance
# bofa = BankAccount("checking", 500)
# bofa.deposit(500)
# print(bofa.accumulate_interest(5))

