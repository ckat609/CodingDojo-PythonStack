from django.shortcuts import render, HttpResponse, redirect

# path('/', views.index),
# path('/new', views.new_blog),
# path('/create', views.create_blog),
# path('/<int:number>', views.show_blog),
# path('/<int:number>/edit', views.edit_blog),
# path('/<int:number>/delete', views.destroy_blog)


def register(request):
    return HttpResponse("placeholder for users to create a new user record")


def login(request):
    return HttpResponse("placeholder for users to log in")


def new_user(request):
    return redirect("/")


def users(request):
    return HttpResponse("placeholder to later display all the list of users")
