from django.db import models


class AboutMe(models.Model):
    name = models.CharField(max_length=20, default="Prakash Rai")
    interests = models.CharField(max_length=100)
    profile = models.TextField(max_length=500)
    blog_description = models.TextField(max_length=500, default="Mathematics and Computer Science Blog")


class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100)
    phone_no = models.IntegerField(blank=True, null=True)
    message = models.TextField(max_length=10000)