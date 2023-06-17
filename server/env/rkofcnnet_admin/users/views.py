from .serializers import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from users.models import Users
from users.serializers import UsersSerializers

@csrf_exempt
def userApi(request, id=0) :
    if request.method == 'GET' :
        users = Users.objects.all().order_by("-id")
        user_serializer = UsersSerializers(users, many=True)
        permission_classes = (AllowAny,)
        return JsonResponse(user_serializer.data, safe=False)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializers(data=user_data)
        permission_classes = (AllowAny,)
        #print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            #print(user_serializer)
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse({"status": "error", "data": user_serializer.errors})

    elif request.method == 'DELETE' :
        users = Users.objects.get(id=id)
        users.delete()
        return JsonResponse("Deleted Successfully", safe=False)

