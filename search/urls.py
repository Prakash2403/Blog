from django.conf.urls import url

from search import views

urlpatterns = [url(r'^', view=views.search, name='search-post'),
               ]
