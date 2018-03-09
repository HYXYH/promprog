# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from todolist.models import Task


class TaskSerializer(ModelSerializer):
    text = serializers.CharField(required=True)
    done = serializers.BooleanField()

    class Meta:
        model = Task
        fields = '__all__'
