from django.urls import path
from clients.views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete', ClientDeleteView.as_view(), name='client-delete'),
]