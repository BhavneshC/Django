from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from clients.models import Client
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    assigned_users = models.ManyToManyField(User, related_name='assigned_users')
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})