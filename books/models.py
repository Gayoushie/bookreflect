from django.core.urlresolvers import reverse
from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	bio = models.TextField()

	def book_count(self):
		book_count = self.book_set.count() 
		return book_count

	def first_letter(self):
		return self.last_name and self.last_name[0] or ''

	def __unicode__(self):
		return self.last_name + " " + self.first_name

class Genre(models.Model):
	name = models.CharField(max_length = 200)

	def book_count(self):
		book_count = self.book_set.count() 
		return book_count

	def __unicode__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length = 200)
	isbn = models.CharField(max_length = 200)
	author = models.ForeignKey(Author)
	genre = models.ForeignKey(Genre)
	description = models.TextField()
	cover = models.ImageField(upload_to = 'covers')
	pub_date = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.title

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <  now

	def topic_count(self):
		topic_count = self.topic_set.count() 
		return topic_count

	def get_absolute_url(self):
		return reverse('books:book_details', args=(self.id,))

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

