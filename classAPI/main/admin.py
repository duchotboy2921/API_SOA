from django.contrib import admin
from main.models import Class
# Register your models here.

@admin.register(Class)
class Class(admin.ModelAdmin):
    list_display = ["code","name","credit_class","total_slot","remain_slot","period","day_of_week","classroom","teacher"]
    admin.register(Class)