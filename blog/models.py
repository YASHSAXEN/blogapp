from django.db import models
import datetime
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = HTMLField()
    created_at = models.DateTimeField(default=datetime.datetime.now(),blank=True)
    comments = models.TextField()
    author = models.CharField(max_length=150)
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    comments_count = models.IntegerField(default=0)
    is_updated = models.BooleanField(default=False)

class ContactUs(models.Model):
    username = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())