from django.shortcuts import render

# Create your views here.

from todos import models
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def show_todos(req):
    queryset = models.Todo.objects.all().order_by('id')
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_todo(req):
    serializer = TodoSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_todo(req, pk):
    try:
        target = models.Todo.objects.get(id=pk)
        target.delete()
        Response(status=status.HTTP_200_OK)
    except:
        Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_todo(req, pk):
    try:
        target = models.Todo.objects.get(id=pk)
        serializer = TodoSerializer(target, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
