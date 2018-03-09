from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django import forms
from .models import Task

# Create your views here.

#
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['text']
#
#
# class TasksView(ListView):
#     template_name = "todolist/todolist.html"
#     task_form = None
#
#     def dispatch(self, request, blog_id=None, *args, **kwargs):
#         self.task_form = TaskForm(self.request.GET)
#         return super(TasksView, self).dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         print(request.POST)
#         self.task_form = TaskForm(request.POST)
#         if self.task_form.is_valid():
#             self.task_form.save()
#         else:
#             print(" Not valid! {}".format(self.task_form))
#         return HttpResponseRedirect('/')
#
#     def get_context_data(self, **kwargs):
#         context = super(TasksView, self).get_context_data(**kwargs)
#         context['task_form'] = self.task_form
#         return context
#
#     def get_queryset(self):
#         return Task.objects.all()
