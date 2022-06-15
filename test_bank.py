import unittest
from bank import Bank


class TestBank(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank(3000)

    def testSum(self):
        self.assertEqual(self.bank.sum(300), 3300)

    def testMinus(self):
        self.assertEqual(self.bank.sum(-200), 3100)

    def testError(self):
        self.assertEqual(self.bank.debt('test'), 'Error')


if __name__ == '__main__':
    unittest.main()
