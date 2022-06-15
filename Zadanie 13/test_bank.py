import unittest
from bank import Saldo


class TestBank(unittest.TestCase):

    def test_BankMinus(self):
        self.assertEqual(Saldo.suma(1000, -100), 900)

    def test_BankPlus(self):
        self.assertEqual(Saldo.suma(1000, 100), 1100)

    def test_BankError(self):
        self.assertEqual(Saldo.suma("abc", 10000), "Błąd!")

if __name__ == '__main__':
    unittest.main()