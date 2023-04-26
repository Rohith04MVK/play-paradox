from django.db import models


class RaceTime(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    time_in_seconds = models.CharField(max_length=100)
