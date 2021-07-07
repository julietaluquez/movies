from django.db import models
from django.utils import timezone


class Post(models.Model):
    original_name = models.CharField(max_length = 50)
    nameinspain = models.CharField(max_length = 50)
    year = models.DateTimeField()
    director = models.CharField(max_length = 80)
    duration = models.TimeField()
    sinopsis = models.TextField()
    genres = models.CharField(max_length = 50)
    rate = models.BooleanField(default=False)
    Rating_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)
rate = models.IntegerField(choices=Rating_CHOICES, default=1)
     

    



  

def publish(self):
        self.published_date = timezone.now()
        self.save()

def __str__(self):
        return self.title

