# Generated by Django 2.1.11 on 2019-10-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellogApp', '0003_auto_20191009_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='placeName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
