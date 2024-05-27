from django.contrib import admin
from .models import Author, Library, Books

# Register your models here.
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Books)