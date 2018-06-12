from django.conf.urls import url

from . import views

# to difference between apps, for polls application use this app name for all the urls
app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create', views.create_task, name='create'),
    url(r'^delete', views.delete_task, name='delete'),
    url(r'^assign', views.assign, name='assign'),
    url(r'^my', views.my_tasks, name='my_tasks'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
]
