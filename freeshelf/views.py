from django.shortcuts import render, redirect
from freeshelf.forms import SearchForm
from freeshelf.models import Book


def index(request):
    books = Book.objects.all().order_by('-date_added')
    return render(request, 'index.html', {'books': books, })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {'book': book, })


def edit_book(request, slug):
    book = Book.objects.get(slug=slug)
    form_class = SearchForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', slug=book.slug)
        else:
            form = form_class(instance=book)
        return render(request, 'books/edit_book.html', {'book': book, 'form': form, })
