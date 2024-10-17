from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostListSerializer, BlogPostDetailSerializer

# Endpoint to get the list of blog posts (title, description, image)
class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializer

# Endpoint to get details of a single blog post based on its title
class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'slug'  # Use title to lookup instead of id
