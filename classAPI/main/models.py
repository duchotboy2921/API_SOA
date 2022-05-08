from django.db import models


# Create your models here.
class Class(models.Model):
    code = models.CharField(null=False, max_length=50)
    name = models.CharField(null=False, max_length=100)
    credit_class = models.IntegerField(null=False)
    total_slot  = models.IntegerField(null= False)
    remain_slot = models.IntegerField(null= False)
    period = models.IntegerField(null=False)
    day_of_week = models.IntegerField( null=False)
    classroom = models.CharField( max_length=100)
    teacher = models.CharField(null=False, max_length=100)

