# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from todolist.models import Task
# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by('created_at')
    serializer_class = TaskSerializer
