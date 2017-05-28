from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^', name='blog-home', view=views.index),
]
