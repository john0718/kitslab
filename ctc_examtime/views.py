from django.shortcuts import render
from datetime import datetime

def current_time_view(request):
    
    return render(request, 'time/current_time.html',)

