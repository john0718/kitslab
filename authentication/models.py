from django.db import models

from django.contrib.auth.models import User

class Role(models.TextChoices):
    FACULTY = 'FACULTY', 'Faculty'
    COORDINATOR = 'COORDINATOR', 'Lab Coordinator'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"