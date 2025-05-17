from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        # можешь добавить свои роли
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
