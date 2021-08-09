from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    class UserType(models.TextChoices):
        ADMIN = 'admin'
        EDITOR = 'editor'
        ORDINARY = 'ordinary'
    role = models.CharField(max_length=10, choices=UserType.choices,
                            default=UserType.ORDINARY)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email


