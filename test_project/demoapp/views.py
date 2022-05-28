from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


from demoapp.models import Cars
from demoapp.serializers import CarSerializer
from demoweb.models import Theater
from demoweb.models import TagName
from demoweb.serializers import TheaterSerializer
from demoweb.serializers import TagNameSerializer
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


@csrf_exempt
def getData(request):
    if request.method == 'GET':
        tagData = TagName.objects.all()
        tag = request.GET.get('tag', None)
        if tag is not None:
            
            tagData = tagData.filter(tag__icontains=tag)

        tSerializer = TagNameSerializer( tagData, many=True)
        return JsonResponse(tSerializer.data, safe = False)
        # return JsonResponse(tSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
