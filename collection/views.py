from django.shortcuts import render

# Create your views here.
def index(request):
    book = "Books name"
    return render(request, 'index.html', {'book': book, })
