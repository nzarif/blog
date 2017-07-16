from django.conf.urls import url
from weblog import views as weblog_views

urlpatterns=[
    url(r'^/blogs/$',weblog_views.weblogs),
    url(r'^(?P<weblog_id>\d+)/$',weblog_views.weblog)
]