from django.conf.urls import patterns, url

from discussions import views

urlpatterns = patterns('',
	# ex: /discussions/
	url(r'^$', views.topics, name='topics'),
	# ex: /discussions/5/
    url(r'^(?P<topic_id>\d+)/$', views.topic_posts, name='topic_posts'),
    # ex: /discussions/5/post/
    url(r'^(?P<topic_id>\d+)/post/$', views.new_post, name='new_post'),
)