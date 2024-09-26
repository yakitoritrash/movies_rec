from django.db import models


# Create your models here.
class Genre(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)


class Movie(models.Model):
    name = models.CharField(max_length=255, null=False)
    year = models.IntegerField(null=False)
    director = models.CharField(max_length=50, null=True)
    thumbnail = models.BinaryField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, null=True)
    country = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.name} - {self.year}"
