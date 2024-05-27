from django.urls import path
from . import views


urlpatterns = [
    
    path('lenguajes/', views.languages_view, name='lenguajes'),
    path('categorias/', views.categories_view, name='categorias'),
    path('proyectos/', views.project_view, name='proyectos'),
    path('tareas/', views.task_view, name='tareas'),
    path('notas/', views.notes_view, name='notas'),

    path('add-project/', views.add_project, name='add-project'),
    path('add-task/', views.add_task, name='add-task'),
    path('add-note/', views.add_note, name='add-note'),

    path('project/<int:project_id>/', views.project_detail, name='project'),


    path('dashboard/', views.dashboard, name='dashboard'),
]
