from django.urls import path
from .views import (
    faculty_dashboard,
    lab_requests,
    view_lab_requests,
    edit_lab_request,
    delete_lab_request,
    download_lab_requests,
    course_entry_list,


)

urlpatterns = [
    path('dashboard/', faculty_dashboard, name='faculty_dashboard1'),
    path('requests/', lab_requests, name='faculty_lab_requests'),
    path('view_requests/', view_lab_requests, name='view_lab_requests'),
    path('edit-request/<int:pk>/', edit_lab_request, name='edit_lab_request'),
    path('delete-request/<int:pk>/', delete_lab_request, name='delete_lab_request'),
    path('download-lab-requests/', download_lab_requests, name='download_lab_requests'),
    path('course-entries/', course_entry_list, name='gcr_course_entry_list'),
  
]