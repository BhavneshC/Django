from django.shortcuts import render
from projects.models import Project
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    ordering = ['-created_at']

    def get_context_data (self, ** kwargs):
        context = super (). get_context_data (** kwargs)
        user = self.request.user
        context ['projects_list'] = Project.objects.filter(assigned_users=user)
        return context

class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    fields = ['project_name', 'assigned_users', 'client_name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project