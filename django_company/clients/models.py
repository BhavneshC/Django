from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse("client-detail", kwargs={"pk": self.pk})