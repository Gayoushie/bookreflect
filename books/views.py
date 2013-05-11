from django.shortcuts import render_to_response, get_object_or_404, render
from books.models import Book, Genre, Author
from discussions.models import Topic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render_to_response('home.html',
        context_instance=RequestContext(request))

def howitworks(request):
    return render_to_response('howitworks.html',
        context_instance=RequestContext(request))

def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    topic_list = Topic.objects.filter(book = book_id).order_by('-start_date')

    paginator = Paginator(topic_list, 5)
    page = request.GET.get('page')

    try:
      topics = paginator.page(page)
    except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      topics = paginator.page(1)
    except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      topics = paginator.page(paginator.num_pages)

    return render_to_response('books/bookdetails.html', {'book': book, 'topic_list': topics},
        context_instance=RequestContext(request))

def genres(request):
    genre_list = Genre.objects.all().order_by('name')
    return render_to_response('books/genre.html', {'genre_list': genre_list},
        context_instance=RequestContext(request))

# def genres_sidebar(request):
#     genre_list = Genre.objects.all().order_by('name')[:3]
#     return render_to_response('books/genre.html', {'genre_list': genre_list, 'view_type': 'sidebar'},
#         context_instance=RequestContext(request))

def genre_books(request, genre_id):
    book_list = Book.objects.filter(genre=genre_id).order_by('title')

    paginator = Paginator(book_list, 9)
    page = request.GET.get('page')

    try:
      book_list = paginator.page(page)
    except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      book_list = paginator.page(1)
    except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      book_list = paginator.page(paginator.num_pages)

    return render_to_response('books/booklist.html', {'book_list': book_list, 'filter_by': 'genre'},
        context_instance=RequestContext(request))

def authors(request):
    author_list = Author.objects.all().order_by('last_name')
    return render_to_response('books/author.html', {'author_list': author_list},
        context_instance=RequestContext(request))

def author_books(request, author_id):
    book_list = Book.objects.filter(author=author_id).order_by('author')
    author = Author.objects.get(id=author_id)

    paginator = Paginator(book_list, 9)
    page = request.GET.get('page')

    try:
      book_list = paginator.page(page)
    except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      book_list = paginator.page(1)
    except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      book_list = paginator.page(paginator.num_pages)

    return render_to_response('books/booklist.html', {'book_list': book_list, 'filter_by': 'author', 'author': author},
        context_instance=RequestContext(request))

# def book_topics(request, book_id):
#     topic_list = Topic.objects.filter(book=book_id)
#     return render_to_response('discussions/topics.html', {'topic_list': topic_list},
#         context_instance=RequestContext(request))

def new_topic(request, book_id):
    b = get_object_or_404(Book, pk=book_id)
    
    new_topic = request.POST['new_topic']
    if len(new_topic) == 0:
        return render_to_response('books/bookdetails.html',
            {
                'book': b,
                'error_message': 'Please type your topic in the area below and click Submit Topic',
            },
            context_instance=RequestContext(request))
    else:
        b.topic_set.create(name = new_topic, author = request.user)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('books:book_details', args=(b.id,)))


