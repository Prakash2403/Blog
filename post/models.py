from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return self.title

    def head(self):
        return self.content[:250]+'...'

    def indexing(self):
        from .index_post import PostIndex
        obj = PostIndex(
            meta={'id': self.id},
            author=self.author,
            datetime=self.datetime,
            title=self.title,
            content=self.content
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    def get_comments(self):
        return self.comments_set.order_by('-datetime')


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=30, null=True, blank=True)
    datetime = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return self.post.title + " " + self.post.author


class Replies(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    author = models.CharField(max_length=30, null=True, blank=True)
    datetime = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=10000)


class UserResponse(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    num_likes = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)