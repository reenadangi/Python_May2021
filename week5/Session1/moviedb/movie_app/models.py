from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Movie(models.Model):
    title = models.CharField(max_length=250)
    description=models.CharField(max_length=255)
    director =models.ForeignKey(Director,related_name="movies", on_delete=models.CASCADE)
    release_date=models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    