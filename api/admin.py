from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'id')  # Fields to display in the list view
    search_fields = ('title',)  # Enable searching by title
