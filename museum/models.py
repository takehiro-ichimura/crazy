from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
class Blog(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=True)
    movie_tag = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('museum.Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text