class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    # nameusr = ""

    def __init__(self,name):
        self.name = name
        self.int_rate = 0.01
        self.balance = 0
        BankAccount.all_accounts.append(self)
    #    BankAccount.nameurs = self.name
   
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        # print(f"your balance now: {self.balance}")
        # your code here
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        # your code here
        return self

    def display_account_info(self):
        print(self.name )
        print(f" Balance : ${self.balance}")
        # your code here
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Insufficient")
        # your code here
        return self

    @classmethod
    def all_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        

    # @classmethod
    # def new_user(cls, name):
    #     cls.nameusr = name


aloAcount = BankAccount("Alondra")
alanAcount = BankAccount("Alan")

# aloAcount.deposit(50).deposit(50).deposit(33).yield_interest().display_account_info()
# alanAcount.deposit(20).deposit(30).withdraw(15).withdraw(15).withdraw(15).withdraw(15).withdraw(15).display_account_info()

aloAcount.deposit(50).deposit(50).deposit(33).yield_interest()

# BankAccount.new_user("alo")
# BankAccount.new_user("luis")
BankAccount.all_info()

