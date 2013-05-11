from django.contrib import admin
from books.models import Author, Genre, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ['last_name']

class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'isbn', 'author', 'genre', 'description', 'cover']
    list_display = ('title', 'get_author_fl')
    list_filter = ['author']
    search_fields = ['title']

    def get_author_fl(self, obj):
        return '%s' % (obj.author.first_name + " " + obj.author.last_name)
    get_author_fl.short_description = 'Author'

admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

admin.site.register(Book, BookAdmin)