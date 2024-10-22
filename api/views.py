from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost, ContactSubmission
from .serializers import BlogPostListSerializer, BlogPostDetailSerializer, ContactSubmissionSerializer
from django.core.mail import send_mail
from django.conf import settings
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
        
        # Send email notification
        self.send_notification_email(serializer.data)
        
        return Response({"message": "Contact submission successful"}, status=status.HTTP_201_CREATED, headers=headers)

    def send_notification_email(self, data):
        subject = 'New Contact Form Submission'
        message = f"""
        A new contact form submission has been received:
        
        Company Name: {data['company_name']}
        Sender Name: {data['sender_name']}
        Position: {data['position']}
        Company Email: {data['company_email']}
        Message: {data['message']}
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = settings.CONTACT_FORM_RECIPIENTS

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)
