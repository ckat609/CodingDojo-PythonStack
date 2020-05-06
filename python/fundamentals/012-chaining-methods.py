class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        return self.account_balance

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)
        return self


armando = User("Armando", "Tello", "ckat609@yahoo.com")
david = User("David", "Thompson", "dthompson80@yahoo.com")
natasha = User("Natasha", "Charles", "ncharles@gmail.com")

armando.make_deposit(300)
print(f"{armando.first_name} {armando.last_name} currently has: ${armando.display_user_balance()}")

david.make_deposit(600)
print(f"{david.first_name} {david.last_name} currently has: ${david.display_user_balance()}")

natasha.make_deposit((450))
print(f"{natasha.first_name} {natasha.last_name} currently has: ${natasha.display_user_balance()}")


print(f"{armando.first_name} {armando.last_name} currently has: ${armando.make_deposit(100).make_deposit(210).make_withdrawl(75).make_withdrawl(100).display_user_balance()}")

print(f"{natasha.first_name} {natasha.last_name} currently has: ${natasha.make_withdrawl(50).make_withdrawl(150).make_withdrawl(25).display_user_balance()}")


david.transfer_money(armando, 300)
print(f"{david.first_name} {david.last_name} currently has: ${david.display_user_balance()}")
print(f"{armando.first_name} {armando.last_name} currently has: ${armando.display_user_balance()}")


armando.transfer_money(natasha, 150)
print(f"{armando.first_name} {armando.last_name} currently has: ${armando.display_user_balance()}")
print(f"{natasha.first_name} {natasha.last_name} currently has: ${natasha.display_user_balance()}")
