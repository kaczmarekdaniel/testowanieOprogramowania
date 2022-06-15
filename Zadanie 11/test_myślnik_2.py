import unittest
import myślnik2

class TestMyslnik2(unittest.TestCase):

    def setUp(self):
        self.addresses = ["cokolwiek", "drugie cokolwiek"]

    def test_myslnik2(self):
        result = True
        self.assertEqual(myślnik2.myslnik(self.addresses[1]), result == False)

if __name__ == '__main__':
    unittest.main()