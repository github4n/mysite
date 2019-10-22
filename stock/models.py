from django.db import models

# Create your models here.
class Apply(models.Model):
    biztype = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    apply_time = models.CharField(max_length=14)


