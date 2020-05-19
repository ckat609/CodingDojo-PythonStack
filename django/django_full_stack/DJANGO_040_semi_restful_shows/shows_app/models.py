from django.db import models
from datetime import datetime

# Create your models here.


class ShowManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}

        if(len(postData['title']) == 0):
            errors['title'] = "Show title must contain at least one character."
        if(len(postData['description']) > 0 and len(postData['description']) < 10):
            errors['description'] = "Show description can be empty, but if it's included, it should contain at least ten characters."
        if(len(postData['image']) == 0):
            errors['image'] = "Image path must be included."
        if(postData['release_date'] >= datetime.now().strftime('%Y-%m-%d')):
            errors['release_date'] = "Date can't be set to today or in the future."

        return errors


class Network(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True)
    image = models.TextField(null=True)
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()
