class BankAccount:
    def __init__(self, amount=0, int_rate=0.01):
        self.balance = amount
        self.int_rate = int_rate

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    def show_balance(self):
        return self.balance


class User:
    def __init__(self, fName, lName, email):
        self.first_name = fName
        self.last_name = lName
        self.email = email
        self.accounts = {}

    def add_account(self, amount=0, int_rate=0.01):
        self.accounts[f"{len(self.accounts)}"] = BankAccount(amount, int_rate)
        return self

    def make_deposit(self, account, amount):
        self.accounts[account].make_deposit(amount)
        return self

    def make_withdrawl(self, account, amount):
        self.accounts[account].make_withdrawl(amount)
        return self

    def yield_interest(self, account):
        self.accounts[account].yield_interest()
        return self

    def show_balance(self, account):
        self.accounts[account].show_balance()


armando = User("Armando", "Tello", "ckat609@yahoo.com")
armando.add_account(100, 0.02)
armando.add_account(100, 0.01)
armando.add_account(100, 0.01)
armando.add_account(100, 0.01)

armando.make_deposit('0', 300).make_deposit('1', 100).yield_interest('2').make_withdrawl('3', 30)

for key, value in armando.accounts.items():
    print(f"Account: {key} - Balance: {value.show_balance()}")
