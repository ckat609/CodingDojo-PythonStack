from django.shortcuts import render, redirect, HttpResponse
from .models import Wishlist
from login_app.models import User
from products_app.models import Product


def index(request):
    # return render(request, "index.html")
    return HttpResponse("HELLO WISHLIST!")
# Create your views here.


def add(request, prod_id):
    aWishlist = Wishlist.objects.get(user_id=request.session['user_id'])
    aProduct = Product.objects.get(id=prod_id)
    aWishlist.products.add(aProduct)
    return redirect("/user/login/success")


def remove(request, prod_id):
    User.objects.get(id=request.session['user_id']).wishlist.products.remove(Product.objects.get(id=prod_id))
    return redirect("/user/login/success")
