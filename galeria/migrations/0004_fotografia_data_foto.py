# Generated by Django 4.2.8 on 2024-01-07 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_foto',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
