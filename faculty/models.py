from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LabRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    degree = models.CharField(max_length=20)
    programme = models.CharField(max_length=50)
    numberofcredits = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    num_slots = models.CharField(max_length=20)
    num_batches = models.CharField(max_length=20,blank=True, null=True)
    os_required = models.CharField(max_length=500,blank=True, null=True)
    software_required_version_opensource = models.CharField(max_length=500,blank=True, null=True)
    software_required_version_license = models.CharField(max_length=500,blank=True, null=True)
    remarks = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}-{self.department_name}-({self.course_name})"