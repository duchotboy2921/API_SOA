from django.http import JsonResponse
from main.models import Class

def getClass(request,code):
    obj = Class.objects.filter(code=code)
    if obj.count() > 0:
        data = {
            "result" : list(obj.values("id", "code", "name", "teacher","slot_number"))
        }
    else :
        data={
            "result": "none"
        }
    return JsonResponse(data)