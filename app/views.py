from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TaskList
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = TaskList
    template_name = 'task_list.html'
    context_object_name = 'todos'
    
class TaskDetailView(DetailView):
    model = TaskList
    template_name = 'task_detail.html'
    context_object_name = 'todo'
    pk_url_kwarg = 'id'
    
class TaskCreateView(CreateView):
    model = TaskList
    template_name = 'task_create.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')
    
class TaskUpdateView(UpdateView):
    model = TaskList
    template_name = 'task_update.html'
    fields = '__all__'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('task_list')
    
class TaskDeleteView(DeleteView):
    model = TaskList
    template_name = 'task_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('task_list')
    context_object_name = 'todo'
    
tasks = TaskList.objects.exclude(status='Сделано')
for task in tasks:
    print(task)