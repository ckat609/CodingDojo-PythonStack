from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from products_app.models import Product
from login_app.models import User
from wishlist_app.models import Wishlist

# Create your views here.


def add(request):
    return render(request, "product_add.html")


def add_db(request):
    errors = Product.objects.basicValidator(request.POST)

    if(len(errors) > 0):
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, "product_add.html")
    else:
        aProduct = Product.objects.create(name=request.POST['name'], image=request.POST['image'], user_id=request.session['user_id'])
        return redirect(f"/product/view/{aProduct.id}")


def view(request, prod_id):
    aProduct = Product.objects.get(id=prod_id)
    aList = Wishlist.objects.filter(products=aProduct)

    exists = True if(len(User.objects.get(id=request.session['user_id']).wishlist.products.filter(id=prod_id))) else False

    context = {
        'id': aProduct.id,
        'name': aProduct.name,
        'image': aProduct.image,
        'user': f"{aProduct.user.first_name} {aProduct.user.last_name}",
        'wishlists': aProduct.wishlist.all(),
        'exists': exists,
    }
    return render(request, "product_view.html", context)


def listall(request):
    aWishlist = Wishlist.objects.get(user_id=request.session['user_id'])
    bWishlist = Product.objects.exclude(wishlist=aWishlist)

    context = {
        'products': bWishlist.order_by('name')
    }
    return render(request, "product_list.html", context)


def delete(request, prod_id):
    aProduct = Product.objects.get(id=prod_id)
    aProduct.delete()
    return redirect("/product/list")
