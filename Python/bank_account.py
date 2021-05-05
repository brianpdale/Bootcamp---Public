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
        
account1 = BankAccount(100)
account2 = BankAccount()

account1.display_account_info()
account2.display_account_info()

account1.deposit(100).deposit(200).deposit(600).withdraw(400).yield_interest().display_account_info()
account2.deposit(200).deposit(400).withdraw(200).withdraw(300).withdraw(100).withdraw(100).yield_interest().display_account_info()
