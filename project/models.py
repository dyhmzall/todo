from django.db import models
from uuid import uuid4
from users.models import Users


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128)
    repository = models.URLField(blank=True)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return self.name


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.text
