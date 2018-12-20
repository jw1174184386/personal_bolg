from django.contrib import admin
from showblog.models import *

admin.site.site_header = '风城浪子'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'address']
    list_display_links = ['name', 'city', 'address']
    list_filter = ['name']
    search_fields = ['name', 'city']
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_display_links = ['name', 'email']
    list_filter = ['salutation']
    list_per_page = 10
    search_fields = ['salutation']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'publication_date']
    list_display_links = ['title', 'publisher', 'publication_date']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
