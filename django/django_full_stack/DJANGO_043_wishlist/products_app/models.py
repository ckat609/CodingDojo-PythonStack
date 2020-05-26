from django.db import models
from login_app.models import User


class ProductManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if(len(postData['name']) < 3):
            errors['name'] = "Invalid product name: the product name must be at least 3 characters long."
        if(len(postData['image']) == 0):
            errors['image'] = "Invalid image url:  the specified url appears to be invalid."
        return errors


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField(null=True)
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()
