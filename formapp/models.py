from django.db import models

# Create your models here.

class Car(models.Model):
    cname=models.CharField(max_length=40)
    price=models.IntegerField()
    model=models.CharField(max_length=30)
    variant=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    engine=models.CharField(max_length=25)
