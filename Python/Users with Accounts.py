class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.accounts = []
    def make_deposit(self, amount):
        self.account_deposit(amount)
        

    def make_withdrawal(self, amount):
        self.account_withdraw(amount)
    
    def make_transfer(self, amount, name):
        self.account.balance -= amount
        name.account.balance += amount
    def check_balance(self, balance):
        self.balance = balance
    def display_user_balance(self):
        print(self.name, self.account.balance)



class BankAccount:
    def __init__(self, balance = 0, int_rate = .01): 
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
    def all_balances(cls):
        sum = 0
        for account in cls.all_account:
            sum += account.balance
        return sum

Devin = User("Devin Dale", "Devin@DDale.com")
Jane = User("Jane Hylton", "Jane@python.com")
Brian = User("Brian Dale", "Brian@python.com")
account1 = BankAccount(100)
account2 = BankAccount()

Devin.account.deposit(100)
Devin.account.display_account_info
Devin.account.deposit(200)
Devin.account.deposit(50)
Devin.account.withdraw(100)
Devin.make_transfer(200, Jane) # Makes transfer if amount to selected user.
Devin.display_user_balance()
Jane.display_user_balance()

# Jane.make_deposit(500)
# Jane.make_deposit(200)
# Jane.make_withdrawal(100)
# Jane.make_withdrawal(25)
# Jane.display_user_balance()

# Brian.make_deposit(600)
# Brian.make_withdrawal(200)
# Brian.make_withdrawal(50)
# Brian.make_withdrawal(100)
# Brian.display_user_balance()
