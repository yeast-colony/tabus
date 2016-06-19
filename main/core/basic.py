from main.models import *
from django.db.models import Count

default_tag = "__no_tag__"
def search(tags, username):
	"""
		@Description
			search for sentences marked with 
			@tags and created by @username
		@Args
			@tags <- list of string
			@username <- string
		@Returns
			@list of string representation of sentences
	"""
	userDB = User.objects.filter(username=username)
	if userDB == []: 
		raise NotImplementedError()
	else: 
		userDB = userDB[0]

	tagsDB = []
	for tag in tags:
		tagsDB.append(Tag.objects.filter(tag=tag, 
			owner=userDB.id)[0].id)


	tagSentenceDB = TagSentence.objects.filter(tag__in = tagsDB).values('sentence')
	print (tagSentenceDB)
	_tagSentenceDB = tagSentenceDB.annotate(numSentence = Count('sentence'))

	import ipdb; ipdb.set_trace()

def addEntry(username, sentence, tags=default_tag):
	pass

def removeEntry(username, sentence):
	pass

def addTag(username, tag):
	pass

def removeTag(username, tag):
	pass

