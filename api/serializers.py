from rest_framework import serializers
from .models import BlogPost, ContactSubmission

class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title','slug', 'description', 'image']  # For the list view

class BlogPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug','description', 'image', 'content', 'created_at']  # For the detail view

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['company_name', 'sender_name', 'position', 'company_email', 'message']