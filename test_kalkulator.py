import unittest
import calculator


class TestCalc(unittest.TestCase):

    def test_dod(self):
        self.assertEqual(calculator.dod(3, 5), 8)
        self.assertEqual(calculator.dod(-1, 1), 0)

    def test_ode(self):
        self.assertEqual(calculator.ode(3, 5), -2)
        self.assertEqual(calculator.ode(-1, 1), -2)

    def test_mno(self):
        self.assertEqual(calculator.mno(3, 5), 15)
        self.assertEqual(calculator.mno(3, 1), 3)

    def test_dziel(self):
        self.assertRaises(calculator.dziel(10, 0), 0)
        self.assertEqual(calculator.dziel(6, 2), 3)

    def test_pot(self):
        self.assertEqual(calculator.pot(5), 25)
        self.assertEqual(calculator.pot(4), 16)

    def test_pierw(self):
        self.assertEqual(calculator.pierw(25), 5)

    def test_proc(self):
        self.assertEqual(calculator.proc(5, 1), 500)
        self.assertEqual(calculator.proc(4, 1), 400)


if __name__ == '__main__':
    unittest.main()
