class Bank:
    def __init__(self, balance) -> None:
        self.balance = balance
    
    def getBalance(self):
        if isinstance(self.balance, int):
            return self.balance
        return "Error"

    def debt(self, amount):
        if isinstance(amount, int):
            return amount
        return "Error"

    def sum(self, amount):
        if isinstance(self.balance, int) and isinstance(amount, int):
            self.balance += amount
            return self.balance
        return "Error"
