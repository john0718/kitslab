
from django.urls import path
from .views import (
        faculty_dashboard,
        allocate_exam_view,
        check_availability,
        confirm_allocation,
        course_allotment_view,
        credentials_generation_view,
        generate_credentials_excel,
        credentials_manager_view,
        generate_credentials,
        send_credentials_email,
        download_credentials_excel, 
        download_all_credentials_pdf,
        upload_excel,    
        division_requests,
        assign_course,
        download_assigned_courses,
        course_entry_list,
        download_course_entries_excel,
    )

urlpatterns = [
    path('', faculty_dashboard, name='faculty_dashboard'),
    path('allocate/<str:course_code>/<str:course_name>/<str:batch_no>/', allocate_exam_view, name='allocate_exam'),
    path('check-availability/', check_availability, name='check_availability'),
    path('confirm_allocation/', confirm_allocation, name='confirm_allocation'),
    path('course-allotment/', course_allotment_view, name='course_allotment'),
    path('credentials-generation/', credentials_generation_view, name='credentials_generation'),
    path('generate-credentials-allocation/<int:allocation_id>/', generate_credentials_excel, name='generate_credentials_excel'),
    path('credentials-manager/', credentials_manager_view, name='credentials_manager'),
    path('generate-credentials-ajax/<int:cred_id>/', generate_credentials, name='generate_credentials_ajax'),
    path('send-credentials-email/<int:cred_id>/', send_credentials_email, name='send_credentials_email'),
    path('download-credentials/<int:cred_id>/', download_credentials_excel, name='download_credentials_excel'),
    path('download-all-credentials/', download_all_credentials_pdf, name='download_all_credentials'),
    path('upload-excel/', upload_excel, name='upload_excel'),
    path('division-requests/', division_requests, name='division_requests'),
    path('assign-course/<int:lab_id>/', assign_course, name='assign_course'),
    path('download-assigned-courses/', download_assigned_courses, name='download_assigned_courses'),
    path('course-entries/', course_entry_list, name='course_entry_list'),
    path('course-entries/download/', download_course_entries_excel, name='download_course_entries_excel'),

]





