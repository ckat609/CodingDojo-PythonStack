from django.shortcuts import render, HttpResponse, redirect

# path('/', views.index),
# path('/new', views.new_blog),
# path('/create', views.create_blog),
# path('/<int:number>', views.show_blog),
# path('/<int:number>/edit', views.edit_blog),
# path('/<int:number>/delete', views.destroy_blog)


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new_blog(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create_blog(request):
    return redirect("/blogs")


def show_blog(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")


def edit_blog(request, number):
    return HttpResponse(f"placeholder to edit blog number: {number}")


def destroy_blog(request, number):
    return redirect("/blogs")
