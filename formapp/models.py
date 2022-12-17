from django.db import models

# Create your models here.

class Car(models.Model):
    cname=models.CharField(max_length=40)
    price=models.IntegerField()
    model=models.CharField(max_length=30)
    variant=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    engine=models.CharField(max_length=25)

    def __str__(self):
        return self.cname+' [ '+ self.model +' ]'


class Customer(models.Model):
    name=models.CharField(max_length=40)
    mob=models.PositiveBigIntegerField()
    English=models.BooleanField()
    Kannada=models.BooleanField()
    Hindi=models.BooleanField()
    Telugu=models.BooleanField()
    Tamil=models.BooleanField()
