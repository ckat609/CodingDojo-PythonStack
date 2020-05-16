from django.shortcuts import render, redirect
from books_authors_app.models import *


def index(request):
    return render(request, "index.html")


def add_book_form(request):
    # books = Book.objects.all()
    context = {
        'books': Book.objects.all()
    }
    print(context)
    return render(request, "add_book.html", context)


def add_author_form(request):
    # books = Book.objects.all()
    context = {
        'authors': Author.objects.all()
    }
    print(context)
    return render(request, "add_author.html", context)


def view_book(request, id):
    context = {
        'book': Book.objects.get(id=id),
        'author': Author.objects.exclude(books=Book.objects.get(id=id))
    }
    print(context)
    return render(request, "view_book.html", context)


def view_author(request, id):
    context = {
        'author': Author.objects.get(id=id),
        'book': Book.objects.exclude(authors=Author.objects.get(id=id))
    }
    print(context)
    return render(request, "view_author.html", context)


def add_book_db(request):
    # /print("*"*50)
    if(request.POST['book-title'] != "" and request.POST['book-desc'] != ""):
        Book.objects.create(title=request.POST['book-title'], desc=request.POST['book-desc'])
    return redirect("/book/")


def add_author_db(request):
    # /print("*"*50)
    if(request.POST['author-first'] != "" and request.POST['author-last'] != "" and request.POST['author-notes'] != ""):
        Author.objects.create(first_name=request.POST['author-first'], last_name=request.POST['author-last'], notes=request.POST['author-notes'])
    return redirect("/author/")


def add_author_to_book(request, id):
    print("*"*50)
    print(request.POST['new_author'])
    Book.objects.get(id=id).authors.add(Author.objects.get(id=request.POST['new_author']))
    return redirect(f"/book/{id}")


def add_book_to_author(request, id):
    print("*"*50)
    print(request.POST['new_book'])
    Author.objects.get(id=id).books.add(Book.objects.get(id=request.POST['new_book']))
    return redirect(f"/author/{id}")
