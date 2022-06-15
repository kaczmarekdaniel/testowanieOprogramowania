class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie, stala):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie = wynagrodzenie
        self.stala = stala

    def email(self):
        return f"{self.imie}.{self.nazwisko}@testemail.com"

    def pelna_nazwa(self, nazwisko):
        return f"{self} {nazwisko}"

    def podwyzka(self, stala):
        return self * stala
