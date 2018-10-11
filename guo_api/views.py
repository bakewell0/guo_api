from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pymysql

@csrf_exempt
def test_api(request):
    return JsonResponse({"result": 0, "msg": "success"})

@csrf_exempt
def user(request):
    username = request.POST["username"];
    password = request.POST["password"];

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123aaa", "guozhenshi")
    print(db)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
    db.close()
    return JsonResponse({"username": username})

