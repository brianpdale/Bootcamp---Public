
class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def make_transfer(self, amount, name):
        self.account_balance -= amount
        name.account_balance += amount

    def display_user_balance(self):
        print(self.name, self.account_balance)

Devin = User("Devin Dale", "Devin@DDale.com")
Jane = User("Jane Hylton", "Jane@python.com")
Brian = User("Brian Dale", "Brian@python.com")



Devin.make_deposit(100)
Devin.make_deposit(200)
Devin.make_deposit(50)
Devin.make_withdrawal(100)
Devin.make_transfer(20, Jane) # Makes transfer if amount to selected user.
Devin.display_user_balance()

Jane.make_deposit(500)
Jane.make_deposit(200)
Jane.make_withdrawal(100)
Jane.make_withdrawal(25)
Jane.display_user_balance()

Brian.make_deposit(600)
Brian.make_withdrawal(200)
Brian.make_withdrawal(50)
Brian.make_withdrawal(100)
Brian.display_user_balance()

class BankAccount:
    def __init__(self, balance = 0, int_rate = .01): 
        # default_int_rate = .01
        # default_balance = 0
        # self.int_rate = .01
        # self.balance = balance if balance is None else default_balance
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("Balance: $" + str(self.balance) + "  Interest Rate: %" + str(self.int_rate*100))
        return self
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self
    def print_all_account_info(self, balance, int_rate):
        print(self.name, self.account_balance, self.balance, self.int_rate)

account1 = BankAccount(100)
account2 = BankAccount()

account1.display_account_info()
account2.display_account_info()

account1.deposit(100).deposit(200).deposit(600).withdraw(400).yield_interest().display_account_info()
account2.deposit(200).deposit(400).withdraw(200).withdraw(300).withdraw(100).withdraw(100).yield_interest().display_account_info()
account1.print_all_account_info()