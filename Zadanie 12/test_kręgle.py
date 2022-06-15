import unittest
from kręgle import kregle


class test_kregle(unittest.TestCase):
    def setUp(self):
        self.game = kregle()

    def testNormalThrow(self):
        self._roll_many(1, 3)
        self._roll_many(0, 17)
        self.assertEqual(self.game.calculateScore(), 3)

    def testStrike(self):
        self.game.throw(10)
        self.game.throw(3)
        self.game.throw(4)
        self._roll_many(0, 16)
        self.assertEqual(self.game.calculateScore(), 24)

    def testSpare(self):
        self.game.throw(5)
        self.game.throw(5)
        self.game.throw(3)
        self._roll_many(0, 17)
        self.assertEqual(self.game.calculateScore(), 16)

    def _roll_many(self, pins, num):
        for i in range(num):
            self.game.throw(pins)

if __name__ == '__main__':
    unittest.main()