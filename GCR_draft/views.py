from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import CourseEntry
import logging
from django.contrib.auth.decorators import login_required

# Set up logging to help debug
logger = logging.getLogger(__name__)


@login_required
def course_form(request):
    print("User:", request.user)
    print("Is Authenticated:", request.user.is_authenticated)
    batch_range = range(1, 21)

    if request.method == 'POST':
        try:
            # Debug: Print all POST data to console
            print("POST data received:", request.POST)
            
            # FIXED: Map HTML form field names to model field names
            form_data = {
                'school': request.POST.get('school'),
                'division': request.POST.get('division'),
                'year': request.POST.get('year'),
                'semester': request.POST.get('semester'),
                'degree': request.POST.get('degree'),
                'branch': request.POST.get('branch'),
                'course_code': request.POST.get('course_code'),
                'course_name': request.POST.get('course_name'),
                'credits': request.POST.get('credits'),
                'batch_no': request.POST.get('batch_no'),
                'course_type': request.POST.get('course_type'),
                'mode': request.POST.get('mode'),
                'faculty_id': request.POST.get('faculty_id'),
                'faculty_name': request.POST.get('faculty_name'),
                # FIXED: HTML form uses 'faculty_contact', model expects 'faculty_contact_number'
                'faculty_contact_number': request.POST.get('faculty_contact_number'),
                # FIXED: HTML form uses 'faculty_email', model expects 'faculty_email'
                'faculty_email': request.POST.get('faculty_email'),
                'timetable': request.POST.get('timetable'),
            }
            
            # Debug: Print form data
            print("Form data:", form_data)
            
            # FIXED: Map HTML option values to model choice values
            # Your HTML form uses different values than your model expects
            choice_mappings = {
                'school': {
                    'SET': 'School of Engineering and Technology',
                    'SCST': 'School of Computer Science and Technology', 
                    'SAMM': 'School of Sciences Arts Media and Management',
                    'SABS': 'School of Agriculture and Bio Sciences'
                },
                'year': {
                    '1': 'I year', '2': 'II year', '3': 'III year', '4': 'IV year', '5': 'V year'
                },
                'degree': {
                    'btech': 'B.Tech', 'mtech': 'M.Tech', 'bcom': 'B.Com',
                    'bca': 'BCA', 'bsc': 'B.Sc', 'ba': 'B.A',
                    'ma': 'M.A', 'mba': 'MBA', 'msc': 'M.Sc',
                    'research': 'Research', 'others': 'Others'
                },
                'course_type': {
                    'theory': 'Theory', 'practical': 'Practical', 'placement': 'Placement'
                },
                'mode': {
                    'offline': 'offline', 'blended': 'blended'
                }
            }
            
            # Apply mappings
            for field, mapping in choice_mappings.items():
                if form_data.get(field) in mapping:
                    form_data[field] = mapping[form_data[field]]
            
            # Convert division/branch values to full names
            division_mapping = {
                'aerospace': 'Aerospace Engineering',
                'agriculture': 'Agriculture',
                'bioinformatics': 'Bioinformatics',
                'biotechnology': 'Biotechnology',
                'chemistry': 'Chemistry',
                'civil': 'Civil Engineering',
                'commerce': 'Commerce',
                'cse': 'Computer Science and Engineering',
                'aiml': 'Artificial Intelligence and Machine Learning',
                'dscs': 'Data Science and Cyber Security',
                'eee': 'Electrical and Electronics Engineering',
                'ece': 'Electronics and Communication Engineering',
                'robotics': 'Robotics',
                'biomedical': 'Biomedical Engineering',
                'english': 'English',
                'food-processing': 'Food Processing',
                'it': 'Information Technology',
                'management': 'Management Studies',
                'mathematics': 'Mathematics',
                'mechanical': 'Mechanical Engineering',
                'media': 'Media and Communication',
                'nano': 'Nano Sciences',
                'physics': 'Physics',
                'value-education': 'Value Education',
                'water': 'Water Institute',
                'isdf': 'ISDF',
                'computer-application': 'Computer Application',
                'criminology': 'Criminology',
                'digital-sciences': 'Digital Sciences',
                'data-analytics': 'Data Science and Analytics',
                'clinical-psychology': 'Clinical Psychology',
                'others': 'Others'
            }
            
            if form_data.get('division') in division_mapping:
                form_data['division'] = division_mapping[form_data['division']]
            if form_data.get('branch') in division_mapping:
                form_data['branch'] = division_mapping[form_data['branch']]
            
            # Check for required fields (adjust based on your model)
            required_fields = ['school', 'course_code', 'course_name']
            missing_fields = [field for field in required_fields if not form_data.get(field)]
            
            if missing_fields:
                error_msg = f"Missing required fields: {', '.join(missing_fields)}"
                print("Error:", error_msg)
                return HttpResponse(f"Error: {error_msg}")
            
            # Create and save the model instance
            course_entry = CourseEntry.objects.create(**form_data)
            
            print(f"Successfully created CourseEntry with ID: {course_entry.id}")
            # return HttpResponse("Form submitted and saved successfully!")
            
        except Exception as e:
            # Debug: Print any errors
            print(f"Error saving to database: {str(e)}")
            logger.error(f"Error in course_form view: {str(e)}")
            return HttpResponse(f"Error saving to database: {str(e)}")

    return render(request, 'course_form.html', {'batch_range': batch_range})





# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import CourseEntry  # Import your model

# def course_form(request):
#     batch_range = range(1, 21)

#     if request.method == 'POST':
#         # Create and save the model instance
#         CourseEntry.objects.create(
            
#             school = request.POST.get('school'),
#             division = request.POST.get('division'),
#             year = request.POST.get('year'),
#             semester = request.POST.get('semester'),
#             degree = request.POST.get('degree'),
#             branch = request.POST.get('branch'),
#             course_code = request.POST.get('course_code'),
#             course_name = request.POST.get('course_name'),
#             credits = request.POST.get('credits'),
#             batch_no = request.POST.get('batch_no'),
#             course_type = request.POST.get('course_type'),
#             mode = request.POST.get('mode'),
#             faculty_id = request.POST.get('faculty_id'),
#             faculty_name = request.POST.get('faculty_name'),
#             faculty_contact_number = request.POST.get('faculty_contact_number'),
#             faculty_email = request.POST.get('faculty_email'),
#             timetable = request.POST.get('timetable'),
#         )

#         return HttpResponse("Form submitted and saved successfully!")

#     return render(request, 'course_form.html', {'batch_range': batch_range})
