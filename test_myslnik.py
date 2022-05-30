import unittest
import myslnik


class TestMyslnik(unittest.TestCase):

    def setUp(self):
        self.tekst = "tutaj jest tekst"

    def test_myslnik(self):
        self.assertEqual(myslnik.myslnik(self.tekst), False)


if __name__ == '__main__':
    unittest.main()
