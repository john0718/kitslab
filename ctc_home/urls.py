from django.urls import path
from .views import *


urlpatterns = [
    path('',ctc_home,name='ctc_home')
]
