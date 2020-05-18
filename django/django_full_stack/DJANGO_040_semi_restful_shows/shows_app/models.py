from django.db import models

# Create your models here.


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

