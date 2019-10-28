from .models import Values, Project
from .serializers import ValuesSerializer, ValuesListSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class ValuesListByUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        values = Values.objects.filter(user=request.user)
        serializer = ValuesListSerializer(values, many=True)
        
        for item in serializer.data:
            if item.get('type') == '1':
                item['type'] = 'Alimentação'
            
            elif item.get('type') == '2':
                item['type'] = 'Estadia'
                
            elif item.get('type') == '3':
                item['type'] = 'Transporte'
            
            elif item.get('type') == '4':
                item['type'] = 'Outros'

        return Response(serializer.data)


class ValuesCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = ValuesSerializer(data=request.data)
        
        if serializer.is_valid():
            project = get_object_or_404(Project, id=request.data.get('project'))
            user = get_object_or_404(User, id=request.user.id)
            
            serializer.save(project=project, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValuesDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, format=None):
        value = get_object_or_404(Values, id=request.data.get('id'))
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)