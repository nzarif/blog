"""blog URL Configuration

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
from django.conf.urls import url , include
from django.contrib import admin
from weblog import views as weblog_views
from authc import views as auth_views


urlpatterns = [
    url(r'^$',auth_views.register),
    url(r'^auth/register$',auth_views.register),
    url(r'^auth/login$',auth_views.login),
    url(r'^blog/(?P<bid>\d+)/posts', weblog_views.getposts),
    url(r'^blog/(?P<bid>\d+)/post', weblog_views.share),
    url(r'^blog/(?P<bid>\d+)/comments',weblog_views.getcomments),
    url(r'^blog/(?P<bid>\d+)/comment',weblog_views.comment),
    url(r'^admin/', admin.site.urls),
]
