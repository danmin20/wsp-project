# Generated by Django 3.2.4 on 2021-06-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='movie_title',
            field=models.CharField(default=models.CharField(max_length=200), max_length=200),
        ),
    ]
