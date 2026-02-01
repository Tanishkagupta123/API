from rest_framework import serializers 
from .models import Player_Serializer


class Player(serializers.ModelSerializer):
    class Meta:
        model=Player_Serializer
        fields='_all_'