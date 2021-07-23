from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Vehicule(models.Model):

    class NumQuai(models.IntegerChoices):
        AUCUN = 0
        NORD = 1
        EST = 2
        SUD = 3
        OUEST = 4

    type = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    plaque = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='images/', null=True)
    authorization = models.BooleanField()
    quai = models.IntegerField(choices=NumQuai.choices, default=0)

    def __str__(self):
        return self.plaque
