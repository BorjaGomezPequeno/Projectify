from django.conf import settings
from django import forms
from .models import Project, Task, Notes

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'client_name', 'description', 'categories', 'languages', 'assigned_to']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 5}),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'languages': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'task_name', 'task_description', 'assigned_to']
        widgets = {
            'project': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
            'task_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'task_description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 5}),
            'assigned_to': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note_name', 'note_description', 'project', 'assigned_to']
        widgets = {
            'note_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'note_description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 5}),
            'project': forms.Select(attrs={'class': 'form-select form-select=lg mb-3'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }