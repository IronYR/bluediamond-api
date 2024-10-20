from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost, ContactSubmission
from .serializers import BlogPostListSerializer, BlogPostDetailSerializer, ContactSubmissionSerializer

# Endpoint to get the list of blog posts (title, description, image)
class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializer

# Endpoint to get details of a single blog post based on its title
class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'slug'  # Use title to lookup instead of id

# Endpoint to handle contact form submissions
class ContactSubmissionView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Contact submission successful"}, status=status.HTTP_201_CREATED, headers=headers)
