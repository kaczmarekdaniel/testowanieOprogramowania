import unittest
import myslnik2


class TestMyslnik2(unittest.TestCase):

    def setUp(self):
        self.addresses = ["Roberto Babiaggio", "Vicitore Frelichio", "Maciek-Misztalski"]

    def test_if_myslnik(self):
        result = True
        self.assertEqual(myslnik2.if_myslnik(self.addresses[1]), result == False)


if __name__ == '__main__':
    unittest.main()
