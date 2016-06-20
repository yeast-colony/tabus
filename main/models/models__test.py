from django.utils import timezone
from django.test import TestCase

from django.utils import timezone

from main.models.models import *
import main.models.modelsOps as modelsOps
import main.models.testingUtils as testingUtils


class TestCase__models(TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test__addEntry(self):
		modelsOps.addEntries(testingUtils.test__entries)

		self.assertTrue (len(User.objects.all()) == 2 )
		self.assertTrue (len(Sentence.objects.all()) == 4 )
		# self.assertEqual(
		# 	[ str(db) for db in User.objects.all()], 
		# 	test__usern)

	# def test__search(self):
	# 	self.assertEqual(
	# 		search(["lasek", "analogia"], "Szymon"),
	# 		["co to jest kupka?"]
	# 	)
	# 	self.assertEqual(
	# 		search(["pieknedrzewa"], "Szymon"),
	# 		[]
	# 	)
	# 	self.assertEqual(
	# 		search(["pieknedrzewa"], "Agata"),
	# 		["kto to zje panie profesorze?",
	# 			"Czy jesteś kominiarzem?"]
	# 	)
	# 	self.assertEqual(
	# 		search(["lasek", "analogia"], "Agata"),
	# 		["co to jest kupka?"]
	# 	)


	# def test_general(self):
	# 	addEntries(test__entries)
		
	# 	self.assertTrue ( 
	# 		len(User.objects.all()) == len(test__usernames) )		
	# 	self.assertTrue ( 
	# 		len(Sentence.objects.all()) == 4 )
	# 	self.assertEqual(
	# 		[ str(db) for db in User.objects.all()], 
	# 		test__usern)
#-----------------------------------------------------------------
