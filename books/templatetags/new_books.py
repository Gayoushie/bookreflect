from django import template
from books.models import Book

register = template.Library()

@register.inclusion_tag('../mytemplates/books/new_books.html', takes_context=True)
def new_books(context):
    new_books_list = Book.objects.all().order_by('-pub_date')[:3]
    #return {'new_books_list': new_books_list} 
    return {
    	'MEDIA_URL': context['MEDIA_URL'], 
    	'new_books_list': new_books_list,
    }