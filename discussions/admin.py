from django.contrib import admin
from books.models import Book
from discussions.models import Topic, Post
from django.contrib.auth.models import User

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'author', 'start_date')
    search_fields = ['name']

class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'post_content', 'author', 'post_date')
    search_fields = ['post_content']

admin.site.register(Topic, TopicAdmin)

admin.site.register(Post, PostAdmin)