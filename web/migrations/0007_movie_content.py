# Generated by Django 4.2.6 on 2023-11-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0006_alter_movie_card_movie_quality"),
    ]

    operations = [
        migrations.CreateModel(
            name="movie_content",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="media")),
                ("title_one", models.CharField(max_length=50)),
                ("title_two", models.CharField(max_length=50)),
                ("head_one", models.CharField(max_length=50)),
                ("content_one", models.CharField(max_length=250)),
                ("head_two", models.CharField(max_length=50)),
                ("content_two", models.CharField(max_length=250)),
            ],
        ),
    ]
