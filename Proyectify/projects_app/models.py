from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    description = models.CharField(max_length=250, verbose_name="Descripcion")
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el:")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.title

class CodeLang(models.Model):
    lang_name = models.CharField(max_length=30, verbose_name="Lenguaje")
    lang_image = models.ImageField(default='null', verbose_name="Imagen")

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"

    def __str__(self):
        return self.lang_name
    

class Project(models.Model):
    project_name = models.CharField(max_length=150, verbose_name="Nombre del proyecto")
    client_name = models.CharField(max_length=120, verbose_name="Nombre del cliente")
    description = models.TextField(verbose_name="Descripcion del proyecto")
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True)
    languages = models.ManyToManyField(CodeLang, verbose_name="Lenguajes", blank=True)

    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asigned_projects', verbose_name='Asignado a: ', null=True, blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.project_name

class Task(models.Model): 
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task', verbose_name="Proyecto")
    task_name = models.CharField(max_length=200, verbose_name="Nombre de la tarea")
    task_description = models.CharField(max_length=500, verbose_name="Descripcion de la tarea")
    completed = models.BooleanField(default=False, verbose_name="Completado")

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asigned_task', verbose_name='Asignado a: ', null=True, blank=True)


    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

class Notes(models.Model):
    note_name = models.TextField(max_length=50, verbose_name="Titulo")
    note_description = models.TextField(max_length=250, verbose_name="Descripcion")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notes', verbose_name='Proyecto'
    )

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asigned_notes', verbose_name='Asignado a: ', null=True, blank=True)


    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
    