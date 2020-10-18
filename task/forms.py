from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'status','doers','watchers', 'begin_date', 'end_date', 'planned_end_date')