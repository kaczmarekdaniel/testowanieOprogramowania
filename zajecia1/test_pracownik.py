import unittest
from pracownik import Pracownik

class Dane():
        x = "Pawel"
        y = "Pawlowski"
        z = 3000

class TestPracownik (unittest.TestCase):

	def test_mail(self):
		self.assertEqual(Pracownik.mail(Dane.x, Dane.y), "Pawel.Pawlowski@testmail.org")

	def test_nazwa(self):
		self.assertEqual(Pracownik.nazwa(Dane.x,Dane.y), "Pawel Pawlowski")

	def test_podwyzka(self):
		self.assertEqual(Pracownik.podwyzka(Dane.z),6000)

if __name__== '__main__':
	unittest.main()
