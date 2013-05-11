from django import template
from discussions.models import Topic
from books.models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()

@register.inclusion_tag('../mytemplates/discussions/topics.html', takes_context=True)
def book_topics(context, book_id, error_message, request): 
	print "Printing request ..."
	print request
	topic_list = Topic.objects.filter(book = book_id).order_by('-start_date')
	book = Book.objects.get(pk = book_id)

	# paginator = Paginator(topic_list, 5)

	# page = request.GET.get('page')

	# try:
	# 	topics = paginator.page(page)
	# except PageNotAnInteger:
	# 	# If page is not an integer, deliver first page.
	# 	topics = paginator.page(1)
	# except EmptyPage:
	# 	# If page is out of range (e.g. 9999), deliver last page of results.
	# 	topics = paginator.page(paginator.num_pages)

	# return {'new_books_list': new_books_list} 
	return {
		'MEDIA_URL': context['MEDIA_URL'], 
		'topic_list': topic_list,
		'book': book,
		'error_message':error_message
	}