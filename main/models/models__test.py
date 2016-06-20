from django.utils import timezone
from django.test import TestCase

from django.utils import timezone

from main.models.models import *
import main.models.modelsOps as modelsOps
import main.models.testingUtils as testingUtils


class TestCase__models(TestCase):
	def setUp(self):
		modelsOps.addEntries(testingUtils.test__entries)

	def tearDown(self):
		pass

	def test__addEntry(self):
		self.assertTrue (len(User.objects.all()) == 2 )
		self.assertTrue (len(Sentence.objects.all()) == 4 )

		# @TODO add more tests

		# self.assertEqual(
		# 	[ str(db) for db in User.objects.all()], 
		# 	test__usern)

	def test__search(self):
		"""
		1) test if finds sentences as providing
			all tags while adding the sentence
		2) check if giving to search only one tag
			which match many sentences, many
			sentences will be returned
		"""

		#(1)
		for test__entry in testingUtils.test__entries:
			username, sentence, tags = test__entry
			self.assertEqual(
				modelsOps.search(tags, username),
				[sentence]
			)

		#(2)
		self.assertEqual(
			modelsOps.search(["wazne"], "Agata"),
			testingUtils.test__sentenes__agata_wazne
		)


