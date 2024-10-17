from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique= True, null=True)
    image = models.URLField(max_length=500)  # URL link to the image
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title