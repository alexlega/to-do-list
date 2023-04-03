from django import forms
from django.forms import SelectDateWidget

from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        widgets = {"deadline": forms.DateTimeInput(attrs={"type": "datetime-local"})}
        fields = ["name", "deadline", "tags"]
