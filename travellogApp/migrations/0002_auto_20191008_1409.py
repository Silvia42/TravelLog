# Generated by Django 2.1.11 on 2019-10-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellogApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='placeImageUrl',
        ),
        migrations.AlterField(
            model_name='place',
            name='placeName',
            field=models.CharField(max_length=50),
        ),
    ]