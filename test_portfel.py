import unittest
import portfel


class TestPortfel(unittest.TestCase):
    def setUp(self) -> None:
        self.portfel = portfel.Portfel()

    def testDefault(self):
        self.assertEqual(self.portfel.getBalance(), 0)

    def testTransfer(self):
        self.portfel.transferMoney(5)
        self.assertEqual(self.portfel.getBalance(), 5)
        self.portfel.setDefault()

    def testSpend(self):
        self.portfel.spendMoney(4)
        self.portfel.transferMoney(5)
        self.assertEqual(self.portfel.getBalance(), 1)
        self.portfel.setDefault()

    def testSettingDefault(self):
        self.portfel.setDefault()
        self.assertEqual(self.portfel.getBalance(), 0)


if __name__ == '__main__':
    unittest.main()
