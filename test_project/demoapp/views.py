from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


from demoapp.models import Cars
from demoapp.serializers import CarSerializer
# Create your views here.

@csrf_exempt
def cars_list(request):
    if request.method == 'POST':
        car_data = JSONParser().parse(request)
        car_serializer = CarSerializer(data= car_data)
        if car_serializer.is_valid():
            car_serializer.save()
            return JsonResponse(car_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(car_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        car_data = Cars.objects.all()
        car_serializer = CarSerializer(car_data, many = True)
        return JsonResponse(car_serializer.data, safe = False)