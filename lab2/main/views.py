from django.shortcuts import render
from datetime import date
from main.models import Task, List

# context = {
#     'done': {
#         'todos': [
#             {
#                 'task': 'task1',
#                 'created': date.today().strftime("%d/%m/%y"),
#                 'due_on': date.today().strftime("%d/%m/%y"),
#                 'owner': 'admin',
#                 'mark': 'Done'
#             },
#             {
#                 'task': 'task2',
#                 'created': date.today().strftime("%d/%m/%y"),
#                 'due_on': date.today().strftime("%d/%m/%y"),
#                 'owner': 'admin',
#                 'mark': 'Done'
#             },
#             {
#                 'task': 'task3',
#                 'created': date.today().strftime("%d/%m/%y"),
#                 'due_on': date.today().strftime("%d/%m/%y"),
#                 'owner': 'admin',
#                 'mark': 'Done'
#             },
#         ]
#     },
#     'not_done': {
#         'todos': [
#             {
#                 'task': 'task4',
#                 'created': date.today().strftime("%d/%m/%y"),
#                 'due_on': date.today().strftime("%d/%m/%y"),
#                 'owner': 'admin',
#                 'mark': 'Not Done'
#             },
#         ]
#     }
# }


# Create your views here.
def todo_list(request, id):
    tasks = Task.objects.filter(list_id=id, mark=False)
    context = {'list': List.objects.get(id=id), 'todos': tasks}
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request, id):
    tasks = Task.objects.filter(list_id=id, mark=True)
    context = {'list': List.objects.get(id=id), 'todos': tasks}
    return render(request, 'completed_todo_list.html', context=context)

