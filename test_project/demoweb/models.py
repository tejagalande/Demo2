from django.db import models

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)
    mobile = models.BigIntegerField(default=0)
    address = models.TextField(default='',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TagName(models.Model):
    bid = models.ForeignKey('Theater',on_delete=models.CASCADE)
    tag = models.CharField(max_length=255, default='', blank=True)
