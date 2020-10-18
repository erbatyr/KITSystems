from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# from django.core.mail import send_mail
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.core import serializers

from .models import Task


class AllTasks(generic.ListView):
    template_name = 'task/index.html'
    context_object_name = "all_tasks"

    def get_queryset(self):
        return Task.objects.order_by('begin_date')


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'doers', 'watchers', 'status', 'begin_date', 'end_date', 'planned_end_date']
    template_name = 'task/new_task.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'doers', 'watchers', 'status', 'begin_date', 'end_date', 'planned_end_date']
    template_name = 'task/task_edit.html'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task/detail.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('index')


