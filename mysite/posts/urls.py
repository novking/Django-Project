"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name = "post_list"),
    url(r'^create/$', views.post_create, name="post_create"),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name="detail"),
    url(r'^(?P<pk>\d+)/edit/$', views.post_updated, name = "post_updated"),

    url(r'^delete/$', views.post_delete, name = "post_delete"),
]
