from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField()

    class Meta:
        model = Task
        fields = "__all__"
