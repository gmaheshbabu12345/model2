from django.db import models

# Create your models here.
class Countries(models.Model):
    cname=models.CharField(max_length=100)
class Capitals(models.Model):
    capital=models.OneToOneField(Countries('cname'),on_delete=models.CASCADE)