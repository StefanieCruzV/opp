class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    # nameusr = ""

    def __init__(self, int_rate, balance):  # (self,name):
        # self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    #    BankAccount.nameurs = self.name

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        print(f"deposit your balance now: {self.balance}")
        # your code here
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        print(f"withdraw your balance now: {self.balance}")
        return self

    def display_account_info(self):
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


class User:
   
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts=[BankAccount(int_rate=0.02, balance=10000)]
      

    # other methods

    def make_deposit(self, amount, indx):
    	# your code here
        self.accounts[indx].deposit(amount)
        # print(self.account.balance)

    def make_withdraw(self, amount, indx):
    	# your code here
        self.accounts[indx].withdraw(amount)
        # print(self.account.balance)
    
    def print_balance(self):
    	# your code here
        # print(f"{self.name} has a balance of : {self.account.balance}")
        # print(self.account.balance)
        print(f"{self.name} has")
        for acc in self.accounts:
            acc.display_account_info()

    def add_account(self,account):
        self.accounts.append(account)
        #print(len(self.accounts))#how many acounta the user has
    
    def transfer_money_account(self,fromAccount, toAccount, amount):
        self.accounts[fromAccount].withdraw(amount)
        self.accounts[toAccount].deposit(amount)
        

aloUser = User('alo',"alo@gmail")
aloUser.print_balance()
# alanAcount = BankAccount(int_rate=0.22, balance=50)
aloUser.make_deposit(120, 0)
# aloUser.make_withdraw(50)

# Create a new account and add it to the user list of accounts
newAcount= BankAccount(int_rate=0.05, balance=30)
aloUser.add_account(newAcount)
aloUser.print_balance()
aloUser.make_deposit(120, 1)
aloUser.print_balance()

aloUser.make_withdraw(120, 0)
aloUser.make_withdraw(120, 1)
aloUser.print_balance()

aloUser.transfer_money_account(0, 1, 100)
aloUser.print_balance()

#Create new User
# jovasUser = User('jovas',"jovas@gmail")
# # alanAcount = BankAccount(int_rate=0.22, balance=50)

# jovasUser.make_deposit(9920)
# jovasUser.make_withdraw(20)
# jovasUser.print_balance()

# jovasNewAcount= BankAccount(int_rate=0.01, balance=180)
# jovasUser.add_account(jovasNewAcount)

# aloUser.print_balance()
# jovasUser.print_balance()

# alanAcount.display_account_info()

# aloAcount.deposit(50).deposit(50).deposit(33).yield_interest()

# # BankAccount.new_user("alo")
# # BankAccount.new_user("luis")
# BankAccount.all_info()

