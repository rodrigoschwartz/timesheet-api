from rest_framework import serializers
from .models import Hours
from core.serializers import ProjectSerializer, UserSerializer


class HoursSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hours
        fields = '__all__'
        