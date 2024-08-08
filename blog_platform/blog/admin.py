# blog/admin.py

from django.contrib import admin
from .models import Post

@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='published')

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'created_at']
    actions = [make_published]

admin.site.register(Post, PostAdmin)
