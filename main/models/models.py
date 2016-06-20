from __future__ import unicode_literals

from django.db import models



class User(models.Model):
	username = models.CharField(max_length = 20)
	def __str__(self):
		return str(self.username)

class Sentence(models.Model):
	adding_date = models.DateTimeField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length = 250)
	def __str__(self):
		return str(self.content + " " + self.owner.username )

class Tag(models.Model):
	tag = models.CharField(max_length = 20)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.tag)	

class TagSentence(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)