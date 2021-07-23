# Generated by Django 3.2.3 on 2021-07-06 13:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('plaque', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 7, 6, 13, 54, 22, 843374, tzinfo=utc))),
                ('authorization', models.BooleanField()),
                ('quai', models.IntegerField(choices=[(0, 'Aucun'), (1, 'Nord'), (2, 'Est'), (3, 'Sud'), (4, 'Ouest')], default=0)),
            ],
        ),
    ]