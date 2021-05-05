
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
    
    def Devin_make_transfer_to_Brian(self, amount, name):
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
Devin.Devin_make_transfer_to_Brian(20, Brian) # Makes transfer if amount to selected user.
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