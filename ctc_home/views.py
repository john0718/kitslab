from django.shortcuts import render

# Create your views here.
def ctc_home(request):
    return render(request,'ctc_home/index.html')