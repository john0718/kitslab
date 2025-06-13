from kitslab.models import AssignedCourses


# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import LabRequestForm
from authentication.models import UserProfile 
from .models import LabRequest
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from openpyxl import Workbook
from GCR_draft.models import CourseEntry


@login_required
def faculty_dashboard(request):
    return render(request, 'faculty/dashboard.html')

@login_required
def lab_requests(request):
    user = request.user
    department = ''

    try:
        department = user.userprofile.department
    except UserProfile.DoesNotExist:
        department = ''

    if request.method == 'POST':
        form = LabRequestForm(request.POST)
        if form.is_valid():
            lab_request = form.save(commit=False)
            lab_request.user = request.user
            lab_request.save()
            messages.success(request, 'Your Request has been submitted successfully.')
            return redirect('faculty_lab_requests')
    else:
        form = LabRequestForm(initial={'department_name': department})
        print(form.errors) 

    return render(request, 'faculty/lab_requests.html', {'form': form, 'department': department})




@login_required
def view_lab_requests(request):
    user = request.user
    lab_requests = LabRequest.objects.filter(user=user)
    assignments = {
        (a.course_code, a.semester, a.year, a.degree.strip().lower(), a.programme.strip().lower()): a.assigned_date
        for a in AssignedCourses.objects.all()
    }

    for req in lab_requests:
        key = (req.course_code, str(req.semester), str(req.year), req.degree.strip().lower(), req.programme.strip().lower())
        assigned_date = assignments.get(key)
        if assigned_date:
            req.is_assigned = True
            req.assigned_date = assigned_date.strftime("%d-%m-%Y")
        else:
            req.is_assigned = False
            req.assigned_date = None

    return render(request, 'faculty/view_requests.html', {'lab_requests': lab_requests})



@login_required
def edit_lab_request(request, pk):
    lab_request = get_object_or_404(LabRequest, pk=pk, user=request.user)
    if request.method == 'POST':
        form = LabRequestForm(request.POST, instance=lab_request)
        if form.is_valid():
            form.save()
            return redirect('view_lab_requests')
    else:
        form = LabRequestForm(instance=lab_request)
    return render(request, 'faculty/edit_request.html', {'form': form})

@login_required
def delete_lab_request(request, pk):
    lab_request = get_object_or_404(LabRequest, pk=pk, user=request.user)
    lab_request.delete()
    return redirect('faculty_lab_requests')




@login_required
def download_lab_requests(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Lab Requests"

    headers = [
        "Department", "Semester", "Year", "Degree", "Programme", "Number of Credits",
        "Course Code", "Course Name", "No of Slots", "No of Batches", "OS Required",
        "Software(Open Source)", "Software(License)", "Remarks"
    ]
    ws.append(headers)

    for req in LabRequest.objects.all():
        ws.append([
            req.department_name, req.semester, req.year, req.degree, req.programme,
            req.numberofcredits, req.course_code, req.course_name, req.num_slots,
            req.num_batches, req.os_required, req.software_required_version_opensource,
            req.software_required_version_license, req.remarks
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=lab_requests.xlsx'
    wb.save(response)
    return response




# Google classroom Allotments works
def course_entry_list(request):
    courses = CourseEntry.objects.all()
    return render(request, 'faculty/gcr_course.html', {'courses': courses})