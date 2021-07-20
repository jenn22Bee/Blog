from django.db import models
from django.urls import reverse


# each blog post will be created here
class BlogPost(models.Model):
    # id - Django automatically creates an auto-incrementing primary key for every model!
    title = models.CharField(max_length=200, unique=True, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=False)
    body = models.TextField()  # content
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    # should we have an status?
    # author?

    # sort post by the created time
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
