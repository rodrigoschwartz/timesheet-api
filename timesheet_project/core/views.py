from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectListByUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        projects = Project.objects.filter(user=request.user.id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        
        if serializer.is_valid():
            user = get_object_or_404(User, id=request.data.get('user'))
            
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)