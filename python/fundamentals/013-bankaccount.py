class BankAccount:
    def __init__(self, amount=0, interest=0.01):
        self.amount = amount
        self.interest = interest
        self.display_user_balance = interest

    def deposit(self, amount):
        self.amount += amount
        return self

    def withdraw(self, amount):
        if(self.amount < 0):
            print("Insufficient funds: Chargin a $5 fee")
            self.amount -= 5
        else:
            self.amount -= amount
        return self

    def display_account_info(self):
        print(self.amount)
        return self

    def yield_interest(self):
        if(self.amount > 0):
            self.amount += self.amount*self.interest
        return self


armandoBA = BankAccount(500)
saurabBA = BankAccount(900)

print(f"{armandoBA.deposit(100).deposit(100).deposit(50).withdraw(75).yield_interest().display_account_info()}")
print(f"{saurabBA.deposit(150).deposit(100).withdraw(75).withdraw(100).withdraw(50).withdraw(50).yield_interest().display_account_info()}")
