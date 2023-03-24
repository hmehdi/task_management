
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TaskSerializer,TaskMiniSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def list(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serialize = TaskMiniSerializer(tasks,many=True)
        return Response(serialize.data)