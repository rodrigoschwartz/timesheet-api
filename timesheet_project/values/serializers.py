from rest_framework import serializers
from .models import Values
from core.serializers import ProjectSerializer, UserSerializer


class ValuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Values
        fields = '__all__'
        depth = 1