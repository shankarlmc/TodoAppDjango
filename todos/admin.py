from django.contrib import admin
from .models import Todo


class to_do(admin.ModelAdmin):
    list_filter = ['completed']

admin.site.register(Todo,to_do)
