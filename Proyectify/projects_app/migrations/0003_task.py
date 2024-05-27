# Generated by Django 5.0.3 on 2024-04-17 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0002_alter_category_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200, verbose_name='Nombre de la tarea')),
                ('task_description', models.CharField(max_length=500, verbose_name='Descripcion de la tarea')),
                ('completed', models.BooleanField(default=False, verbose_name='Completado')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='projects_app.project')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]
