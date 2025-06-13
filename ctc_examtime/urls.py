from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_time_view, name='current_time'),
]
