from django.contrib import admin
from .models import BlogPost, ContactSubmission

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'id')  # Fields to display in the list view
    search_fields = ('title',)  # Enable searching by title

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'sender_name', 'position', 'company_email', 'created_at')
    search_fields = ('company_name', 'sender_name', 'company_email')
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)
