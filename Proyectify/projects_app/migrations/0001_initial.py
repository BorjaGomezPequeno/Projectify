# Generated by Django 5.0.3 on 2024-04-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('description', models.CharField(max_length=250, verbose_name='Descripcion')),
                ('created_at', models.DateField()),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='CodeLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=30, verbose_name='Lenguaje')),
                ('lang_image', models.ImageField(default='null', upload_to='', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150, verbose_name='Nombre del proyecto')),
                ('client_name', models.CharField(max_length=120, verbose_name='Nombre del cliente')),
                ('description', models.TextField(verbose_name='Descripcion del proyecto')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('categories', models.ManyToManyField(blank=True, to='projects_app.category', verbose_name='Categorias')),
                ('languages', models.ManyToManyField(blank=True, to='projects_app.codelang', verbose_name='Lenguajes')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
