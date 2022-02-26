from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
class LikedModel(models.Model):
    user_id = models.IntegerField()
    event_id = models.IntegerField()

class EventModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2500)
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.FileField(upload_to='media/gallery')
    category = models.ManyToManyField(Categories)
    published = models.BooleanField()
    is_paid = models.BooleanField()

    def __str__(self):
        return self.title