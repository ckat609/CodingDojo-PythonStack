from django.db import models

# Create your models here.


class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"({self.id}) - {self.name} - {self.house} - {self.pet} - {self.year}"
