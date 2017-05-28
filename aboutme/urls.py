from django.conf.urls import url, include

from aboutme import views

urlpatterns = [
    url(r'^', name='aboutme', view=views.aboutme_view),
    url(r'^contactme/', name='contactme', view=views.contactme_view)
]
