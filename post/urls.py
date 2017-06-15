from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^(?P<post_id>[0-9]+)/$', views.get_single_post, name='single-post'),
    url(r'^$', view=views.get_all_posts, name='all-post'),
]
