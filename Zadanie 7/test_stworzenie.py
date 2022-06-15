import unittest
from stworzenie import Plik

class TestPlik(unittest.TestCase):
    def setUp(self):
        self.kluby = Plik("ManCity", "Bayern")
    def test_stworzPlik(self):
        self.plik = self.kluby.stworzplik()
        plik = open("Kluby.txt", "r")
        tablica = []
        for i in plik:
            tablica.append(i)
        self.assertEqual(tablica[1].strip("\n"),"Bayern")
    def tearDown(self):
        self.kluby = None
if __name__ == '__main__':
    unittest.main()

