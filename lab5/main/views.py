from django.shortcuts import render
from datetime import date

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from main.models import Task, List
from main.serializers import ListSerializer, TodoSerializer, TaskSerializer


# Create your views here.
def todo_list(request, id):
    tasks = Task.objects.filter(list_id=id, mark=False)
    context = {'list': List.objects.get(id=id), 'todos': tasks}
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request, id):
    tasks = Task.objects.filter(list_id=id, mark=True)
    context = {'list': List.objects.get(id=id), 'todos': tasks}
    return render(request, 'completed_todo_list.html', context=context)


class TodoViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = List.objects.all()
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id):
        queryset = List.objects.get(id=id)
        serializer = ListSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        queryset = List.objects.create(
            name=self.request.data.get('name')
        )
        serializer = ListSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, id):
        queryset = List.objects.get(id=id)
        queryset.name = self.request.data.get('name')
        queryset.save()
        serializer = ListSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, id):
        List.objects.get(id=id).delete()
        queryset = List.objects.all()
        serializer = ListSerializer(queryset)
        return Response(serializer.data)



class TaskViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request, id):
        queryset = Task.objects.filter(list_id=id, mark=False)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def list_marked(self, request, id):
        queryset = Task.objects.filter(list_id=id, mark=True)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id, id2):
        queryset = Task.objects.get(id=id2, list_id=id)
        serializer = TaskSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, id):
        queryset = Task.objects.create(
            list=id,
            task=self.request.data.get('task'),
            created=self.request.data.get('created'),
            due_on=self.request.data.get('due_on'),
            owner=self.request.data.get('owner'),
            mark=False
        )
        serializer = TaskSerializer(queryset)
        return Response(serializer.data)

    def update(self,request,id, id2):
        queryset = Task.objects.get(id=id2, list_id=id)
        queryset.list = List.objects.get(id=self.request.data.get('list'))
        queryset.task = self.request.data.get('task')
        queryset.created = self.request.data.get('created')
        queryset.due_on = self.request.data.get('due_on')
        queryset.owner = self.request.data.get('owner')
        queryset.mark = self.request.data.get('mark')
        queryset.save()
        serializer = TaskSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, id, id2):
        queryset = Task.objects.get(id=id2, list_id=id)
        queryset.delete()
        serializer = TaskSerializer(queryset)
        return Response(serializer.data)

