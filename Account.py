class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance+=money
        return f'Вы внесли {money}р\nБаланс: {self.balance}'

    def __str__(self) -> str:
        return f'Владелец счёта: {self.owner}\nБаланс: {self.balance}'
    
    def withdraw(self, money):
        if money <= self.balance:
            self.balance-=money
            return f'Вы сняли {money}р\nБаланс: {self.balance}'
        else:
            return 'Недостаточно средств!'
    
ilman = Account('Ilman', 5000)
print(ilman.deposit(100))
print(ilman)
print(ilman.withdraw(4900))
print(ilman.withdraw(4900))
print(ilman.owner)
print(ilman.balance)