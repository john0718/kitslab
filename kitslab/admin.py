from django.contrib import admin
from .models import *

admin.site.register(LabDetails)
admin.site.register(StudentsDetails)
admin.site.register(Availability)
admin.site.register(ExamAllocation)
admin.site.register(CredentialsManager) 
admin.site.register(GeneratedCredential)
admin.site.register(AssignedCourses)