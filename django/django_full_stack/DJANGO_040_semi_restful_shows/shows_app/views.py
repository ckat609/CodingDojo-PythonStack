from django.shortcuts import render, redirect, HttpResponse
from shows_app.models import *
from django.utils import timezone
from django.contrib import messages
from datetime import datetime


def index(request):

    return render(request, "index.html")


def show_list(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'show_list.html', context)


def show_view(request, show_num):
    context = {
        'show': Show.objects.get(id=show_num),
    }
    return render(request, 'show_view.html', context)


def show_add(request):
    context = {
        'networks': Network.objects.all(),
        'default_date': datetime.now().strftime('%Y-%m-%d'),
    }
    return render(request, 'show_add.html', context)


def show_edit(request, show_num):
    context = {
        'show': Show.objects.get(id=show_num),
        'networks': Network.objects.all(),
        'date': Show.objects.get(id=show_num).release_date.strftime('%Y-%m-%d')
    }
    return render(request, 'show_edit.html', context)


def show_add_db(request):
    errors = Show.objects.basicValidator(request.POST)
    if(len(errors) > 0):
        for key, value in errors.items():
            messages.error(request, value)
        context = {
            'title': request.POST['title'],
            'image': request.POST['image'],
            'release_date': request.POST['release_date'],
            'default_date': datetime.now().strftime('%Y-%m-%d'),
            'description': request.POST['description'],
            'networkSelected': int(request.POST['network']),
            'networks': Network.objects.all(),
        }
        print("*"*35)
        print(datetime.now().strftime('%Y-%m-%d'))
        print("*"*35)
        return render(request, 'show_add.html', context)
    else:
        Show.objects.create(title=request.POST['title'], image=request.POST['image'], description=request.POST['description'],
                            release_date=request.POST['release_date'], network=Network.objects.get(id=request.POST['network']))
        return redirect(f"/show/view/{Show.objects.last().id}")


def show_edit_db(request):
    errors = Show.objects.basicValidator(request.POST)
    if (len(errors) > 0):
        for kay, value in errors.items():
            messages.error(request, value)
        context = {
            'id': request.POST['id'],
            'title': request.POST['title'],
            'image': request.POST['image'],
            'release_date': request.POST['release_date'],
            'default_date': datetime.now().strftime('%Y-%m-%d'),
            'description': request.POST['description'],
            'networkSelected': int(request.POST['network']),
            'networks': Network.objects.all(),
        }
        return render(request, 'show_edit.html', context)
    else:
        print("*"*35)
        print(request.POST['id'])
        print("*"*35)
        aShow = Show.objects.get(id=request.POST['id'])

        aShow.title = request.POST['title']
        aShow.description = request.POST['description']
        aShow.network = Network.objects.get(id=request.POST['network'])
        aShow.release_date = request.POST['release_date']
        aShow.image = request.POST['image']
        aShow.modified_at = datetime.now().strftime('%Y-%m-%d')
        aShow.save()
        return redirect(f"/show/view/{aShow.id}")


def show_delete_db(request, show_num):
    Show.objects.get(id=show_num).delete()
    return redirect(f"/show/list")
