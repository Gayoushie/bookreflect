from django import template
from django.db.models import Count

register = template.Library()
from books.models import Genre

@register.inclusion_tag('../mytemplates/books/genres_sidebar.html')

def genres_sidebar(count):
	genres_sidebar_list = Genre.objects.all().annotate(num_books=Count('book')).order_by('-num_books')[:count]
	return {'genres_sidebar_list': genres_sidebar_list}