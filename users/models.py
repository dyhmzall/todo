from django.db import models
from uuid import uuid4


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=128)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
