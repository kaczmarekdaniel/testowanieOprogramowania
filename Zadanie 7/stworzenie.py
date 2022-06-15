class Plik:
    def __init__(self, klub1, klub2):
        self.klub1 = klub1
        self.klub2 = klub2

    def stworzplik(self):
        stworzonyplik = open("Kluby.txt", "w+")
        stworzonyplik.write (f"{self.klub1}\n")
        stworzonyplik.write (f"{self.klub2}\n")
        stworzonyplik.close()