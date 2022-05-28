from dataclasses import field
from demoweb.models import Theater
from demoweb.models import TagName
from rest_framework import serializers

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ('id', 'name', 'mobile','address', 'created_at')

class TagNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagName
        fields = ('id','bid','tag')
