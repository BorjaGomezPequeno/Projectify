from django.contrib import admin
from .models import Category, CodeLang, Project, Task, Notes

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    readonly_fields = ('created_at',)

class CodeLangAdmin(admin.ModelAdmin):
    list_display = ('lang_name', 'lang_image')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client_name', 'description')
    raw_id_fields = ('assigned_to',)
    filter_horizontal = ('categories', 'languages')
    readonly_fields = ('created_at', 'updated_at')

class TaskAdmin(admin.ModelAdmin):
    raw_id_fields = ('project','assigned_to')
    list_display = ('task_name', 'task_description', 'completed')

class NotesAdmin(admin.ModelAdmin):
    list_display = ('note_name', 'note_description')
    raw_id_fields = ('project',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(CodeLang, CodeLangAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Notes, NotesAdmin)
