# Generated by Django 4.2.6 on 2023-11-06 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_movie_card_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_card',
            name='details',
            field=models.CharField(max_length=600),
        ),
    ]
