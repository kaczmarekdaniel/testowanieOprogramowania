import unittest
import myślnik

class TestMyslnik(unittest.TestCase):

    def setUp(self):
        self.tekst = "jakikolwiek tekst"

    def test_myslnik(self):
        self.assertEqual(myślnik.myslnik(self.tekst), False)

if __name__ == '__main__':
    unittest.main()