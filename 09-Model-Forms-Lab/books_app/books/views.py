from django.shortcuts import render, redirect

from books_app.books.forms import BookForm
from books_app.books.models import Book


def index(req):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(req, 'index.html', context)


def create(req):
    if req.method == 'GET':
        form = BookForm()
        context = {
            'form': form
        }
        return render(req, 'create.html', context)
    else:
        form = BookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


def edit(req, pk):
    book = Book.objects.get(pk=pk)
    if req.method == 'GET':
        form = BookForm(instance=book)
        context = {
            'form': form
        }
        return render(req, 'edit.html', context)
    else:
        form = BookForm(req.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
