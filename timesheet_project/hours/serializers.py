from rest_framework import serializers
from .models import Hours
from core.serializers import ProjectSerializer, UserSerializer


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = ('id', 'hours', 'project', 'user', 'created_at')
        depth = 1


class HoursListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d/%m/%Y", input_formats=['%d/%m/%Y',])

    class Meta:
        model = Hours
        fields = ('id', 'hours', 'project', 'user', 'created_at')
        depth = 1
        