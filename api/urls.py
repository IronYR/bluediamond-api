from django.urls import path
from .views import BlogPostListView, BlogPostDetailView

urlpatterns = [
    path('api/blogposts/', BlogPostListView.as_view(), name='blogpost-list'),
    path('api/blogposts/<str:slug>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
]
