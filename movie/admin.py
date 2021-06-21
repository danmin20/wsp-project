from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published_date',
        'created_date',
        'author'
    )
    list_display_links = (
        'title',
        'author'
    )