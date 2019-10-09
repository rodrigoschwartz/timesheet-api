import json
from django.http import JsonResponse
from django.http import request
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer


class ProjectListAll(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectListUser(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


@api_view(["GET"])
def get_proj(request):
    project = Project.objects.first()
    if project is None:
        return JsonResponse({"error": "No data found!"}, status=204)
    return JsonResponse(json.loads(project.json), safe=False)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
