from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"({self.id}) - {self.title} - {self.release_date} - {self.duration}\n"
