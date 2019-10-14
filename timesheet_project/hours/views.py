from .models import Hours
from .serializers import HoursSerializer
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HoursListByUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        hours = Hours.objects.filter(user=request.user.id)
        serializer = HoursSerializer(hours, many=True)
        return Response(serializer.data)


class HoursCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        self.hours.user = request.user.id
        