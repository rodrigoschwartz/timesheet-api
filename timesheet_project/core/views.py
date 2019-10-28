from .models import Project
from hours.models import Hours
from values.models import Values
from .serializers import ProjectSerializer, UserSerializer, ProjectStatusSerializer
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectListByUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):
        projects = Project.objects.filter(user=request.user.id)
        serializer = ProjectSerializer(projects, many=True)

        for item in serializer.data:
            # Soma das horas e gastos apontados
            item['hoursApont'] = Hours.objects.filter(project=item.get('id')).aggregate(Sum('hours'))
            item['valuesApont'] = Values.objects.filter(project=item.get('id')).aggregate(Sum('value')) 

            if item.get('status') == '1':
                item['status'] = 'Planejamento'
            
            elif item.get('status') == '2':
                item['status'] = 'Execução'
                
            elif item.get('status') == '3':
                item['status'] = 'Testes'
            
            elif item.get('status') == '4':
                item['status'] = 'Go Live'
            
            elif item.get('status') == '5':
                item['status'] = 'Concluído'

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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ProjectDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, format=None):
        project = get_object_or_404(Project, id=request.data.get('id'))
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectUpdate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        project = get_object_or_404(Project, id=pk)
        project.status = request.data.get('status')
        serializer = ProjectStatusSerializer(project, data=request.data)

        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)