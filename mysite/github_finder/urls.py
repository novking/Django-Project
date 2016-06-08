from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.github, name ='github' ),
    url(r'^github_test/$', views.github_test, name = 'github_test'),
    url(r'^github_profile/$', views.github_profile, name = 'github_profile'),
    ]
