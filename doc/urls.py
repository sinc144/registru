"""registru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from .views import (
    doc_home,
    doc_detail,
    doc_create,
    doc_update,
    doc_delete,
    doc_about,
    doc_contact,
    doc_registru
)


urlpatterns = [
    url(r'^$', doc_home, name='home'),
    url(r'^about/$', doc_about, name='about'),
    url(r'^registru/$', doc_registru, name='registru'),
    url(r'^contact/$', doc_contact, name='contact'),
    url(r'^(?P<id>\d+)/$', doc_detail, name='detail'),
    url(r'^create/$', doc_create, name='create'),
    url(r'^(?P<id>\d+)/edit/$', doc_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', doc_delete, name='delete'),
]