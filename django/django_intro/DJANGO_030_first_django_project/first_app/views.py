from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("ROOT: placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("NEW: placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse(f"SHOW: placeholder to display blog number {number}")


def edit(request, number):
    return HttpResponse(f"EDIT: placeholder to edit blog {number}")


def destroy(request, number):
    return redirect("/")
