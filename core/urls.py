from django.contrib import admin
from django.urls import path, re_path
from app import views

urlpatterns = [
    re_path(r'^tasks/$', views.TaskListView.as_view(), name='task_list'),  
    re_path(r'^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),  
    re_path(r'^tasks/create/$', views.TaskCreateView.as_view(), name='task_create'),  
    re_path(r'^tasks/(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),  
    re_path(r'^tasks/(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete'),  
]
