from django.db import models

# Create your models here.


class movie_card(models.Model):
    image = models.ImageField(upload_to="media")
    movie_name = models.CharField(max_length=50)
    movie_year = models.DateField()
    movie_quality = models.CharField(max_length=3)
    movie_time = models.CharField(max_length=20)
    movie_rating = models.CharField(max_length=10)
    details = models.CharField(max_length=600)


class movie_content(models.Model):
    image = models.ImageField(upload_to="media")
    title_one = models.CharField(max_length=50)
    title_two = models.CharField(max_length=50)
    head_one = models.CharField(max_length=50)
    content_one = models.CharField(max_length=250)
    head_two = models.CharField(max_length=50)
    content_two = models.CharField(max_length=250)
