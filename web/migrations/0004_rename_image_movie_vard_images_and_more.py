# Generated by Django 4.2.6 on 2023-10-06 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_movie_cardtwo_movie_vard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie_vard',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='movie_vard',
            old_name='movie_name',
            new_name='movie_names',
        ),
        migrations.RenameField(
            model_name='movie_vard',
            old_name='movie_quality',
            new_name='movie_qualitys',
        ),
        migrations.RenameField(
            model_name='movie_vard',
            old_name='movie_year',
            new_name='movie_years',
        ),
    ]