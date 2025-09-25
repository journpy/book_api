from django.contrib import admin
from .models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'prefix', 'name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'author', 'isbn']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
