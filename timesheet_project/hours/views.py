from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Hours
from .serializers import HoursSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HoursList(generics.ListCreateAPIView):
    queryset = Hours.objects.all()
    serializer_class = HoursSerializer
    permission_classes = [IsAuthenticated]


class HoursDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hours.objects.all()
    serializer_class = HoursSerializer
    permission_classes = [IsAuthenticated]


class HoursListByUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        hours = Hours.objects.filter(user=request.user.id)
        serializer = HoursSerializer(projects, many=True)
        return Response(serializer.data)
