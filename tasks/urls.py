from django.conf.urls import url

from . import views

# to difference between apps, for polls application use this app name for all the urls
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
