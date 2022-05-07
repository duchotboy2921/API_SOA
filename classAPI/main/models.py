from django.db import models


# Create your models here.
class Class(models.Model):
    id = models.IntegerField(primary_key=True ,null=False, blank= False)
    code = models.CharField(null=False, max_length=50)
    name = models.CharField(null=False, max_length=100)
    teacher = models.CharField(null=False, max_length=100)
    slot_number  = models.IntegerField(null= False)

