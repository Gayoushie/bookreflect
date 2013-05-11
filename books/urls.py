from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns('',
	# ex: /books/
	url(r'^$', views.index, name='index'),
    # ex: /books/howitworks
    url(r'^howitworks/$', views.howitworks, name='howitworks'),
	# ex: /books/5/
    url(r'^(?P<book_id>\d+)/$', views.book_details, name='book_details'),
    # ex: /books/genres/
    url(r'^genres/$', views.genres, name='genres'),
    # ex: /books/genres/5/
    url(r'^genre/(?P<genre_id>\d+)/$', views.genre_books, name='genre_books'),
    # ex: /books/authors/
    url(r'^authors/$', views.authors, name='authors'),
    # ex: /books/authors/5/
    url(r'^author/(?P<author_id>\d+)/$', views.author_books, name='author_books'),
    # # ex: /books/5/topics
    # url(r'^(?P<book_id>\d+)/topics$', views.book_topics, name='book_topics'),
    # ex: /books/5/topics/add
    url(r'^(?P<book_id>\d+)/topics/add/$', views.new_topic, name='new_topic'),
)