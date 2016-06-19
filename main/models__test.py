from django.utils import timezone
from django.test import TestCase

from django.utils import timezone

from main.models import *


test__usernames = ["Agatka", "Szymon"]
test__sentences = ["kto to zje panie profesorze?",
	"Czy jesteś kominiarzem?",
	"co to jest kupka?"]
test__tags = [
	"lasek",
	"analogia",
	"naszlość",
	"misja",
	"pieknedrzewa",
	"owadynocne"]

def test__fillDB():
	userA = User(username=test__usernames[0])
	userA.save()
	userB = User(username=test__usernames[1])
	userB.save()

	sentence1 = Sentence(
		adding_date=timezone.now(), owner=userA,
		content=test__sentences[0])
	sentence2 = Sentence(
		adding_date=timezone.now(), owner=userA,
		content=test__sentences[1])
	sentence3 = Sentence(
		adding_date=timezone.now(), owner=userB,
		content=test__sentences[2])
	sentence1.save()
	sentence2.save()
	sentence3.save()

	tag1 = Tag( tag = test__tags[0], owner = userB)
	tag2 = Tag( tag = test__tags[1], owner = userB)
	tag3 = Tag( tag = test__tags[2], owner = userA)
	tag4 = Tag( tag = test__tags[3], owner = userB)
	tag5 = Tag( tag = test__tags[4], owner = userA)
	tag6 = Tag( tag = test__tags[5], owner = userA)
	tag1.save()
	tag2.save()
	tag3.save()
	tag4.save()
	tag5.save()
	tag6.save()

	tagSentence1 = TagSentence(tag = tag3, sentence = sentence1)
	tagSentence2 = TagSentence(tag = tag5, sentence = sentence1)
	tagSentence3 = TagSentence(tag = tag6, sentence = sentence1)
	tagSentence4 = TagSentence(tag = tag3, sentence = sentence2)
	tagSentence5 = TagSentence(tag = tag5, sentence = sentence2)
	tagSentence6 = TagSentence(tag = tag2, sentence = sentence3)
	tagSentence7 = TagSentence(tag = tag1, sentence = sentence3)
	tagSentence8 = TagSentence(tag = tag4, sentence = sentence3)
	tagSentence1.save()
	tagSentence2.save()
	tagSentence3.save()
	tagSentence4.save()
	tagSentence5.save()
	tagSentence6.save()
	tagSentence7.save()
	tagSentence8.save()



class TestCase__models(TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_general(self):
		"""
		Basic test
		"""
		test__fillDB()
		self.assertTrue ( 
			len(User.objects.all()) == len(test__usernames) )		
		self.assertTrue ( 
			len(Sentence.objects.all()) == len(test__sentences) )
		self.assertEqual(
			[ str(db) for db in User.objects.all()], 
			test__usernames)