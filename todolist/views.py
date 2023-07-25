from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from .models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TaskListView(generic.ListView):
    model = Task


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")


class CompleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)

        task.done = not task.done
        task.save()

        return HttpResponseRedirect(reverse_lazy("todolist:task-list"))
