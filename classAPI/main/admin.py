from django.contrib import admin
from main.models import Class
# Register your models here.

@admin.register(Class)
class Class(admin.ModelAdmin):
    list_display = ["id","code","name","teacher","slot_number"]
    admin.register(Class)