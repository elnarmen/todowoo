from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('id', 'title', 'created', 'datecompleted', 'user')
    list_display_links = ('id', 'title')

admin.site.register(Todo, TodoAdmin)