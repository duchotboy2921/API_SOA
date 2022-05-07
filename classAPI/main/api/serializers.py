from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from main.models import Class

class ClassSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
                model = Class
                fields = ('id', 'code', 'name', 'teacher', 'slot_number')