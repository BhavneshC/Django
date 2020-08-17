from django.shortcuts import render
from clients.models import Client
from django.views.generic import CreateView, ListView, DetailView,  UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ClientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Client
    fields = ['client_name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class ClientListView(UserPassesTestMixin, ListView):
    model = Client
    context_object_name = 'clients'
    ordering = ['-created_at']

    def test_func(self):
        return self.request.user.is_superuser

class ClientDetailView(UserPassesTestMixin, DetailView):
    model = Client

    def test_func(self):
        return self.request.user.is_superuser

class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    fields = ['client_name',]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = '/clients'

    def test_func(self):
        return self.request.user.is_superuser