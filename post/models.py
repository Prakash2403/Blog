from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=10000)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=10000)


class Replies(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=10000)
