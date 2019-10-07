from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer, UserSerializer
from rest_framework import generics


class ProjectListAll(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectListUser(generics.ListAPIView):
    serializer_class = ProjectSerializer

    @api_view(["GET"])
    @permission_classes((IsAuthenticated,))
    def get_queryset(request):
        return Project.objects.filter(user=request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
