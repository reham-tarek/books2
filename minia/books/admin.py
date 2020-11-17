from django.contrib import admin
from books.models import books_list , author_book


admin.site.register(books_list)
admin.site.register(author_book)

