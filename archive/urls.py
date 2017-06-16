from django.conf.urls import url

from archive import views

urlpatterns = [
    url(r'^', name='archive-home', view=views.index),
]
