from django import template
from books.models import Book
from discussions.models import Topic, Post
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('../mytemplates/books/popular_books.html', takes_context=True)
def popular_books(context):
    popular_books_list = Book.objects.annotate(num_topic=Count('topic')).order_by('-num_topic')[:3]
    #return {'popular_books_list': popular_books_list} 
    return {
    	'MEDIA_URL': context['MEDIA_URL'], 
    	'popular_books_list': popular_books_list,
    }