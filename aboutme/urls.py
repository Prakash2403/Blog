from django.conf.urls import url, include

from aboutme import views

urlpatterns = [
    url(r'^contact/$', name='contactme', view=views.contactme_view),
    url(r'^', name='aboutme', view=views.aboutme_view),

]
