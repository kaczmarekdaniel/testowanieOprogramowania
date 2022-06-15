import unittest
from trener import Trener

class TestTrener(unittest.TestCase):
    def setUp(self):
        self.daneTrener = Trener("Bayern", "wiktor")
    def test_trener(self):
        result = self.daneTrener.jest_trener()
        self.assertEqual(result,True)
    def tearDown(self):
        self.daneTrener.klub = ""
        self.daneTrener.trener = None
if __name__ == '__main__':
    unittest.main()