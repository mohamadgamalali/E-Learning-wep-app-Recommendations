from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/(?P<user_Id>[0-9]+)/$', views.detail, name='detail'),
]