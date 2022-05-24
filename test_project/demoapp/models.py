from django.db import models

# Create your models here.

class Cars(models.Model):
    brand= models.CharField(max_length=200, blank=True, default='')
    model_name = models.CharField(max_length=200, blank=True, default='')
