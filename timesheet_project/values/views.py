from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Values
from .serializers import ValuesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ValuesList(generics.ListCreateAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer
    permission_classes = [IsAuthenticated]


class ValuesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer
    permission_classes = [IsAuthenticated]


class ValuesListByUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        values = Values.objects.filter(user=request.user.id)
        serializer = ValuesSerializer(projects, many=True)
        return Response(serializer.data)