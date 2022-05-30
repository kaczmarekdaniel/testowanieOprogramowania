import unittest
from pracownik import Pracownik


# class DanePracownika:
#     def __init__(self):
#         self.imie = "Jan"
#         self.nazwisko = "Kowalski"
#         self.wynagrodzenie = 2000
#         self.stala = 2


class TestPracownik(unittest.TestCase):
    def setUp(self):
        # self.nazwa = DanePracownika()
        self.nazwa = Pracownik("Jan", "Kowalski", 2000, 2)

    def test_email(self):
        self.result = self.nazwa.email()
        self.assertEqual(self.result, "Jan.Kowalski@testemail.com")

    def test_pelnaNazwa(self):
        self.assertEqual(Pracownik.pelna_nazwa(self.nazwa.imie, self.nazwa.nazwisko), "Jan Kowalski")

    def test_podwyzka(self):
        self.assertEqual(Pracownik.podwyzka(self.nazwa.wynagrodzenie, self.nazwa.stala), 4000)

    def tearDown(self):
        self.nazwa.imie = ""
        self.nazwa.nazwisko = ""
        self.nazwa.wynagrodzenie = 0
        self.nazwa.stala = 0


if __name__ == '__main__':
    unittest.main()
