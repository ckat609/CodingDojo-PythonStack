from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello World! This is a test for the Books And Authors Assignment.")

# Create your views here.
