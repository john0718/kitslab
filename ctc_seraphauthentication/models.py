from django.db import models

# Create your models here.
class PasswordResetLog(models.Model):
    email = models.EmailField()
    user_dn = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Success")  # Could be 'Success', 'Failed', etc.

    def __str__(self):
        return f"{self.email} at {self.timestamp} - {self.status}"