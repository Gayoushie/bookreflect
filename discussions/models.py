from django.db import models
from books.models import Book
from django.contrib.auth.models import User

class Topic(models.Model):
	name = models.TextField()
	book = models.ForeignKey(Book)
	author = models.ForeignKey(User)
	start_date = models.DateTimeField(auto_now_add = True)

	def post_count(self):
		post_count = self.post_set.count() 
		return post_count

	def __unicode__(self):
		return self.name

class Post(models.Model):
	post_content = models.TextField()
	topic = models.ForeignKey(Topic)
	author = models.ForeignKey(User)
	post_date = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.post_content