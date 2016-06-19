from django.utils import timezone
from django.test import TestCase

from main.core.basic import *
from main.models__test import *



class TestCase__basic(TestCase):
	def setUp(self):
		test__fillDB()

	def tearDown(self):
		pass

	def test_general(self):
		"""
		Basic test
		"""
		self.assertEqual(
			search(["lasek", "analogia"], "Szymon"),
			["co to jest kupka?"]
		)
		self.assertEqual(
			search(["pieknedrzewa"], "Szymon"),
			[]
		)
		self.assertEqual(
			search(["pieknedrzewa"], "Agata"),
			["kto to zje panie profesorze?",
				"Czy jesteś kominiarzem?"]
		)
		self.assertEqual(
			search(["lasek", "analogia"], "Agata"),
			["co to jest kupka?"]
		)

		#
		#@TODO
		#	
		#