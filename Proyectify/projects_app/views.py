from django.shortcuts import render, redirect, get_object_or_404
from .models import CodeLang, Category, Project, Task, Notes
from .forms import ProjectForm, TaskForm, NoteForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#VISTAS DE LAS SECCIONES

def languages_view(request):
    languages = CodeLang.objects.all()
    return render(request, 'lenguajes.html', {'languages':languages})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categorias.html', {'categories':categories})

def project_view(request):
    if request.user.is_superuser:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(assigned_to = request.user)
    return render(request, 'proyectos.html', {'projects':projects})

def task_view(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to = request.user)
    # tasks = Task.objects.all()
    return render(request, 'tareas.html', {'tasks':tasks})

def notes_view(request):
    if request.user.is_superuser:
        notes = Notes.objects.all()
    else:
        notes = Notes.objects.filter(assigned_to = request.user)
    return render(request, 'notas.html', {'notes':notes})

#DASHBOARD

def dashboard(request):
    return render(request, 'dashboard.html')

#PROYECTOS INDIVIDUALES

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project.html', {'project':project})

# Formularios

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProjectForm()
    projects = Project.objects.all()
    categories = Category.objects.all()
    languages = CodeLang.objects.all()

    return render(request, 'add-project.html', {
        'form':form,
        'projects':projects,
        'categories':categories,
        'languages': languages,
        })

def add_task(request):
    if request.method == 'POST':
        taskForm = TaskForm(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('tareas') 
    else:
        taskForm = TaskForm() 
    return render(request, 'add-task.html', {'taskForm': taskForm})

def add_note(request):
    if request.method == 'POST':
        notesForm = NoteForm(request.POST)
        if notesForm.is_valid():
            notesForm.save()
            return redirect('notas')
    else:
            notesForm = NoteForm()
    return render(request, 'add-note.html', {'notesForm':notesForm})


