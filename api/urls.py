from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, ContactSubmissionView

urlpatterns = [
    path('blogposts/', BlogPostListView.as_view(), name='blogpost-list'),
    path('blogposts/<str:slug>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('contact/', ContactSubmissionView.as_view(), name='api-contact'),
]
