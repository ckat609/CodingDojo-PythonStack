from django.db import models
from login_app.models import User
from products_app.models import Product


class WishlistManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if(len(postData['name']) < 3):
            errors['name'] = "Invalid product name: the product name must be at least 3 characters long."
        return errors


class Wishlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name="wishlist", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
