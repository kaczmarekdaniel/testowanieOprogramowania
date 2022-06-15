class Portfel:
    def __init__(self) -> None:
        self.balance = 0

    def transfer(self, amount):
        self.balance += amount

    def spend(self, amount):
        self.balance -= amount

    def Balance(self):
        return self.balance

    def setDefault(self):
        self.balance = 0