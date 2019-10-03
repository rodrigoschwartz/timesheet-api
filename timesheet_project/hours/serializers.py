from rest_framework import serializers
from .models import Hours


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = '__all__'
