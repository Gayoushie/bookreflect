from django import template
from django.db.models import Count

register = template.Library()
from books.models import Author

@register.inclusion_tag('../mytemplates/books/authors_sidebar.html')

def authors_sidebar(count):
	authors_sidebar_list = Author.objects.all().annotate(num_books=Count('book')).order_by('-num_books')[:count]
	return {'authors_sidebar_list': authors_sidebar_list}