from django.conf.urls import url
from tasks.views import TaskListView, TaskDetailView, TaskCreateView

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

    # class-based-views
    url(r'^generic/$', TaskListView.as_view(), name='task_list'),
    url(r'^generic/detail/(?P<pk>[0-9]+)/$', TaskDetailView.as_view(), name='task_detail'),
    url(r'^generic/create/', TaskCreateView.as_view(), name='task_create'),
    # ajax routes
    url(r'^ajax/delete_task', views.delete_task, name='delete_task'),
    url(r'^ajax/change_priority_task', views.change_priority_task, name='change_priority_task'),
]
