from django.contrib import admin
from main.models import Task, List

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'created', 'due_on', 'owner', 'list', 'mark', ]
    ordering = ['task']
    search_fields = ['task', ]
    list_filter = ['created', 'owner', 'mark', 'list__name', ]


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    ordering = ['name']
    search_fields = ['name']
