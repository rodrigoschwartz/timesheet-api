from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Hours
from .serializers import HoursSerializer
from rest_framework import generics


# Create your views here.
class HoursList(generics.ListCreateAPIView):
    queryset = Hours.objects.all()
    serializer_class = HoursSerializer


class HoursDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hours.objects.all()
    serializer_class = HoursSerializer