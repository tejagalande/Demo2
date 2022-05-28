from django.shortcuts import render
from demoweb.models import Theater
from demoweb.models import TagName
from demoweb.serializers import TheaterSerializer
from demoweb.serializers import TagNameSerializer
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.

@csrf_exempt
def information(request):
    if request.method == 'POST':
        tData = JSONParser().parse(request)
        tSerializer = TheaterSerializer(data=tData)
        if tSerializer.is_valid():
            tSerializer.save()
            return JsonResponse(tSerializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tSerializer.errors, status= status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def setTag(request):
    if request.method == 'POST':
        tData = JSONParser().parse(request)
        tSerializer = TagNameSerializer(data= tData)
        if tSerializer.is_valid():
            tSerializer.save()
            return JsonResponse(tSerializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tSerializer.errors, status=status.HTTP_400_BAD_REQUEST)