from django.shortcuts import render, redirect, HttpResponse
from shows_app.models import *
from django.utils import timezone
import datetime


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
    Show.objects.create(title=request.POST['title'], image=request.POST['image'], description=request.POST['description'],
                        release_date=request.POST['release_date'], network=Network.objects.get(id=request.POST['network']))
    return redirect(f"/show/view/{Show.objects.last().id}")


def show_edit_db(request):
    aShow = Show.objects.get(id=request.POST['id'])

    aShow.title = request.POST['title']
    aShow.description = request.POST['description']
    aShow.network = Network.objects.get(id=request.POST['network'])
    aShow.release_date = request.POST['release_date']
    aShow.image = request.POST['image']
    aShow.modified_at = timezone.now()
    aShow.save()
    return redirect(f"/show/view/{aShow.id}")


def show_delete_db(request, show_num):
    Show.objects.get(id=show_num).delete()
    return redirect(f"/show/list")
