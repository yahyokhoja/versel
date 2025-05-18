# user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Покупатель'),
        ('store_owner', 'Владелец магазина'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
