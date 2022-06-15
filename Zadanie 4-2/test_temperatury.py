import unittest
import temperatury

class Testtemp (unittest.TestCase):

	def test_celcfahr(self):
		self.assertEqual(temperatury.celcfahr(6), 42.8)

	def test_celckelv(self):
		self.assertEqual(temperatury.celckelv(100), 373.15)

if __name__== '__main__':
	unittest.main()