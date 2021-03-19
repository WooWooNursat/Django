from rest_framework import serializers
from main.models import List, Task


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task', 'owner')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
