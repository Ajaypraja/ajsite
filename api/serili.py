from rest_framework import serializers
from .models import student

class st(serializers.Serializer):
    name=serializers.CharField( max_length=50)
    roll=serializers.CharField(max_length=50)
    city=serializers.CharField(max_length=50)
    
    
class st(serializers.Serializer):
    name=serializers.CharField( max_length=50)
    roll=serializers.CharField(max_length=50)
    city=serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        
        instance.save()
        return instance

    # def FunctionName(args):
        
    