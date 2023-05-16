from django.contrib import admin
from .models import Services

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    