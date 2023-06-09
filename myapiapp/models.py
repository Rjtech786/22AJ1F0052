from django.db import models

class Number(models.Model):
    value = models.IntegerField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50)