from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

DEFAULT_EXAM_ID = 1
class Sphere(models.Model):
	title = models.CharField(max_length=200)
	amount = models.IntegerField()
	parent = models.ForeignKey("self",null=True)

	def __str__(self):
		return self.title

class Word(models.Model):
	title = models.CharField(max_length=200)
	defenition = models.CharField(max_length=200)
	status = models.BooleanField(default=False)
	added_time = models.DateTimeField(auto_now_add=True)
	belongs =  models.ForeignKey(Sphere)
	added_by =  models.ForeignKey(User)

	def __str__(self):
		return self.title

	def toJSON(self):
		return {"Word": {"id": self.id, "into_russian": self.defenition, "into_english": self.title}}



class User_Word(models.Model):
	user_id = models.ForeignKey(User)
	word_id = models.ForeignKey(Word)
	learned_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user_id)+'-'+str(self.word_id)

