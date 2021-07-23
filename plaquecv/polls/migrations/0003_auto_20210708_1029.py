# Generated by Django 3.2.3 on 2021-07-08 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_vehicule_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 8, 29, 37, 837373, tzinfo=utc)),
        ),
    ]
