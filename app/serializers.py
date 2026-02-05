from rest_framework import serializers

class EmpSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    age = serializers.IntegerField()