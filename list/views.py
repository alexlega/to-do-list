from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from list.forms import TaskForm
from list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    models = Tag
    fields = "__all__"
    queryset = Tag.objects.all()
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


def task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.progress = not task.progress
    task.save()

    return redirect(reverse("list:task-list"))
