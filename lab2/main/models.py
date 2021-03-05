from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="List name")

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

    def __str__(self):
        return self.name


class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.RESTRICT, related_name='tasks', verbose_name='List')
    task = models.CharField(max_length=255, null=True, blank=True, verbose_name="Task")
    created = models.DateField(verbose_name="Created")
    due_on = models.DateField(verbose_name="Due on")
    owner = models.CharField(max_length=255, null=True, blank=True, verbose_name="Owner")
    mark = models.BooleanField(verbose_name="Mark")

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task
