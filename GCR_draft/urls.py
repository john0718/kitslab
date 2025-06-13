# urls.py
from django.urls import path
from . import views


app_name = 'GCR_draft'

urlpatterns = [
    path('course-form/', views.course_form, name='course_form'),
]
