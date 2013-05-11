from django.shortcuts import render_to_response, get_object_or_404, render
from books.models import Book
from discussions.models import Topic, Post
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def topics(request):
	topic_list = Topic.objects.all();
	return render_to_response('discussions/topics.html', {'topic_list': topic_list},
		context_instance = RequestContext(request))

def topic_posts(request, topic_id):
	post_list = Post.objects.filter(topic=topic_id).order_by('-post_date')
	topic = Topic.objects.get(pk = topic_id)

	paginator = Paginator(post_list, 5)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
 		posts = paginator.page(paginator.num_pages)

	return render_to_response('discussions/posts.html', {'post_list': posts, 'topic': topic},
		context_instance = RequestContext(request))

def new_post(request, topic_id):
	t = get_object_or_404(Topic, pk=topic_id)
	
	new_post_content = request.POST['new_post_content']
	if len(new_post_content) == 0:
		post_list = Post.objects.filter(topic=topic_id).order_by('-post_date')
		return render_to_response('discussions/posts.html',
			{
				'topic': t,
				'post_list': post_list,
				'error_message': 'Please type your comment in the area below and click Submit Comment',
			},
			context_instance = RequestContext(request))
	else:
		t.post_set.create(post_content = new_post_content, author = request.user)
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('discussions:topic_posts', args=(t.id,)))