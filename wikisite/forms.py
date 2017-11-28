from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('Title', 'Description', 'Status', 'Author', 'User_name')