# Generated by Django 4.2.6 on 2023-10-11 18:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_rename_image_movie_vard_images_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="movie_vard",
        ),
    ]
