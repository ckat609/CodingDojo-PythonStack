from django.shortcuts import render, HttpResponse

# path('/', views.index),
# path('/new', views.new_blog),
# path('/create', views.create_blog),
# path('/<int:number>', views.show_blog),
# path('/<int:number>/edit', views.edit_blog),
# path('/<int:number>/delete', views.destroy_blog)


def index(request):
    return HttpResponse("placeholder to display all the surveys created")


def new_survey(request):
    return HttpResponse("placeholder for users to add a new survey")
