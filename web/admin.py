from django.contrib import admin

from .models import movie_card, movie_content

# Register your models here.

admin.site.register(movie_card)

admin.site.register(movie_content)
