from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<pk>/',
        'Delete': '/task-delete/<pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task)

    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)       
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
        
    return Response('Item successfully removed')