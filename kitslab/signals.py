from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import StudentsDetails, ExamAllocation, Availability

@receiver([post_save, post_delete], sender=StudentsDetails)
def update_exam_allocation_strength(sender, **kwargs):
    student_count = StudentsDetails.objects.count()
    for allocation in ExamAllocation.objects.all():
        allocation.student_strength = student_count
        allocation.save()

@receiver([post_save, post_delete], sender=StudentsDetails)
def update_availability_strength(sender, **kwargs):
    student_count = StudentsDetails.objects.count()
    for availability in Availability.objects.all():
        availability.student_strength = student_count
        availability.save()
