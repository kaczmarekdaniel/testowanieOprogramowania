import unittest
import portfel


class TestPortfel(unittest.TestCase):
    def setUp(self) -> None:
        self.Portfel = portfel.Portfel()

    def testDefault(self):
        self.assertEqual(self.Portfel.Balance(), 0)

    def testTransfer(self):
        self.Portfel.transfer(5)
        self.assertEqual(self.Portfel.Balance(), 5)
        self.Portfel.setDefault()

    def testSpend(self):
        self.Portfel.spend(4)
        self.Portfel.transfer(5)
        self.assertEqual(self.Portfel.Balance(), 1)
        self.Portfel.setDefault()

    def testSettingDefault(self):
        self.Portfel.setDefault()
        self.assertEqual(self.Portfel.Balance(), 0)

if __name__ == '__main__':
    unittest.main()