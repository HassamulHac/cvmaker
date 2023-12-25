from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _  # Add this import

class CV(models.Model):
    first_name = models.CharField(max_length=100, default='Null')
    last_name = models.CharField(max_length=100, default='Null')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, default='Null')
    address = models.CharField(max_length=255, default='Address')
    education = models.TextField( default='Null')
    experience = models.TextField( default='Null')
    skills = models.TextField( default='Null')

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s CV"

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, verbose_name=_('groups'))
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        verbose_name=_('user permissions'),
        help_text=_('Specific permissions for this user.'),
    )