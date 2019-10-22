from django.db import models


class stock(models.Model):
    broker = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    apply_time = models.CharField(max_length=200)
