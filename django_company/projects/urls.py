from django.urls import path
from projects.views import ProjectListView, ProjectCreateView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]