from rest_framework import serializers
from .models import Employee

class EmpSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
    
    