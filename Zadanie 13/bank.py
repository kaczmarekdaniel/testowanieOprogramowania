class Bank():
    def account(saldo):
        if isinstance(saldo, int):
            return saldo
        return "Błąd!"

class Kredyt():
    def debt(kwota):
        if isinstance(kwota, int):
            return kwota
        return "Błąd!"

class Saldo():
    def suma(saldo, kwota):
        if isinstance(saldo, int) and isinstance(kwota, int):
            return saldo + kwota
        return "Błąd!"