from django.shortcuts import render

from showblog.models import *


def show_blog_message(request):
    books = Book.objects.all()
    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    return render(request, 'base.html',
                  {'books': books, 'publishers': publishers, 'authors': authors})
