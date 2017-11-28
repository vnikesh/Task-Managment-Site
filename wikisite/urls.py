from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/profile/$', views.home, name='home'),
    url(r'^task/$', views.task_list, name='task_list'),
    url(r'^task/(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^task/create/$', views.task_new, name='task_new'),
    url(r'^summary/$', views.summary, name='summary'),

]