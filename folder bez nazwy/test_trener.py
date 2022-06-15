import os
import unittest
from trener import Trener


class TestTrenera(unittest.TestCase):
    def setUp(self):
        self.daneTrenera = Trener("Bayern", "Manchester", "Piast Człuchów", "Roberto")
        with open("kluby.txt", "xt") as f:
            for i in range(len(self.daneTrenera.klub)):
                f.write("\n" + self.daneTrenera.klub[i])
            f.close()

        with open("kluby.txt", "rt") as f:
            data = f.read()
            f.close()
        print(data)

    def test_trener(self):
        result = self.daneTrenera.hastrener()
        self.assertEqual(result, True)

    def test_kluby(self):
        for i in range(len(self.daneTrenera.klub)):
            result = self.daneTrenera.klub[i]
            self.assertEqual(result, self.daneTrenera.klub[i])

    def tearDown(self):
        self.daneTrenera.klub = ""
        self.daneTrenera.trener = None
        os.remove("kluby.txt")


if __name__ == '__main__':
    unittest.main()
