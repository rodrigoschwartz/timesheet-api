from .models import Hours, Project
from .serializers import HoursSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


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
        serializer = HoursSerializer(data=request.data)
        
        if serializer.is_valid():
            project = get_object_or_404(Project, id=request.data.get('project'))
            user = get_object_or_404(User, id=request.user.id)
            
            serializer.save(project=project, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)