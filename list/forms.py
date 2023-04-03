from django import forms
from django.forms import SelectDateWidget

from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    deadline = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("year", "month", "day")),
        required=False
    )

    class Meta:
        model = Task
        fields = ["name", "deadline", "tags"]
