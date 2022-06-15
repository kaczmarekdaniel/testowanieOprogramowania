class Portfel:
    def __init__(self) -> None:
        self.balance = 0

    def transferMoney(self, amount):
        self.balance += amount

    def spendMoney(self, amount):
        self.balance -= amount

    def getBalance(self):
        return self.balance

    def setDefault(self):
        self.balance = 0
