from rest_framework import serializers
from .models import Values
from core.serializers import ProjectSerializer, UserSerializer


class ValuesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Values
        fields = '__all__'
        depth = 1

    
class ValuesListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d/%m/%Y", input_formats=['%d/%m/%Y',])
    
    class Meta:
        model = Values
        fields = '__all__'
        depth = 1