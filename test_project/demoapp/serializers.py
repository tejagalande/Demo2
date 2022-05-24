from rest_framework import serializers
from demoapp.models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'brand',  'model_name')