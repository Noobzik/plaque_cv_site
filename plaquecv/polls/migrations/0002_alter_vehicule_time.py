# Generated by Django 3.2.3 on 2021-07-06 13:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 6, 13, 54, 36, 731499, tzinfo=utc)),
        ),
    ]