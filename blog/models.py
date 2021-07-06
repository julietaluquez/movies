from django.db import models
from django.utils import timezone


class Post(models.Model):
    original_name = models.CharField(max_length = 50)
    nameinspain = models.CharField(max_length = 50)
    year = models.DateTimeField()
    director = models.charfield(max_length = 80)
    duration = models.TimeField()
    sinopsis = models.textfield()
    rate = models.SmallIntegerField(1,2,3,4,5)
    



  

def publish(self):
        self.published_date = timezone.now()
        self.save()

def __str__(self):
        return self.title

