from unicodedata import name
from django.http import JsonResponse
from main.models import Class

def getClass(request,code):
    obj = Class.objects.filter(code=code)
    if obj.count() > 0:
        data = {
            "result" : list(obj.values("id", "code","name","credit_class","total_slot","remain_slot","period","day_of_week","classroom","teacher"))
        }
    else :
        data={
            "result": "none"
        }
    return JsonResponse(data)

def initData(request):
    for i in range(1,8):
        data = Class(code = "INT123", name = "Toan roi rac 1",credit_class = 3, total_slot = 50, remain_slot = 20, period=2, day_of_week = i, classroom = "601-A2",teacher = "Nguyen Minh")
        data.save()

    for i in range(1,7):
        data = Class(code = "INT124", name = "Lap trinh mang",credit_class = 3, total_slot = 50, remain_slot = 20, period=i, day_of_week = 4, classroom = "701-A2",teacher = "Pham Thu Ha")
        data.save()

    for i in range(1,8):
        data = Class(code = "INT125", name = "CTDL & GT",credit_class = 2, total_slot = 50, remain_slot = 20, period=5, day_of_week = i, classroom = "302-A2",teacher = "Tran Vu")
        data.save()

    for i in range(1,8):
        data = Class(code = "INT126", name = "Giai tich 1",credit_class = 3, total_slot = 50, remain_slot = 20, period=6, day_of_week = i, classroom = "401-A2",teacher = "Hoang Nghia")
        data.save()
    result={
            "result": "init ok"
        }
    return JsonResponse(result)