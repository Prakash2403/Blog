from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^', name='blog-post', view=views.index),
]
