from rest_framework import serializers
from .models import Hours
from core.serializers import ProjectSerializer


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = '__all__'
        depth = 1