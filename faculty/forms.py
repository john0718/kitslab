from django import forms
from .models import LabRequest

class LabRequestForm(forms.ModelForm):
    DEPARTMENT_CHOICES = [
        ('', 'Select Department Name'),
        ('Division of Data Science and Cyber Security', 'Division of Data Science and Cyber Security'),
        ('Division of Civil Engineering', 'Division of Civil Engineering'),
        ('Division of Computer Science and Engineering', 'Division of Computer Science and Engineering'),
        ('Division of Artificial Intelligence and Machine Learning', 'Division of Artificial Intelligence and Machine Learning'),
        ('Division of Electronics and Communication Engineering', 'Division of Electronics and Communication Engineering'),
        ('Division of Mechanical Engineering', 'Division of Mechanical Engineering'),
        ('Division of Robotics Engineering', 'Division of Robotics Engineering'),
        ('Division of Biomedical Engineering', 'Division of Biomedical Engineering'),
        ('Division of Food Processing Technology', 'Division of Food Processing Technology'),
        ('Division of Electrical and Electronics Engineering', 'Division of Electrical and Electronics Engineering'),
        ('Division of Agriculture', 'Division of Agriculture'),
        ('Division of Aerospace Engineering', 'Division of Aerospace Engineering'),
        ('Division of Biotechnology', 'Division of Biotechnology'),
        ('Division of Criminology and Forensic Science', 'Division of Criminology and Forensic Science'),
        ('Division of Physical Sciences', 'Division of Physical Sciences'),
        ('Department of Media and Communication', 'Department of Media and Communication'),
        ('Department of Applied Physics', 'Department of Applied Physics'),
        ('Division of Commerce & International Trade', 'Division of Commerce & International Trade'),
        ('Division of Digital Sciences', 'Division of Digital Sciences'),
        ('Division of Media', 'Division of Media'),
        ('Division of Management Studies', 'Division of Management Studies'),
        ('Water Institute - Centre of Excellence', 'Water Institute - Centre of Excellence'),
        ('English', 'English'),
        ('Department of Instrumentation Engineering', 'Department of Instrumentation Engineering'),
        ('Mathematics', 'Mathematics'),
        ('Centre for Nanoscience & Genomics', 'Centre for Nanoscience & Genomics'),
        ('Division of Physical Education', 'Division of Physical Education'),
        ('Central Library', 'Central Library'),
        ('Department of Applied Chemistry', 'Department of Applied Chemistry'),
    ]

    SEMESTER_CHOICES = [
        ('', 'Select Semester'),
        ('I', 'I'),
        ('III', 'III'),
        ('V', 'V'),
        ('VII', 'VII'),
    ]

    YEAR_CHOICES = [
        ('', 'Select Year'),
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
    ]

    DEGREE_CHOICES = [
        ('', 'Select Degree'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('B.Sc', 'B.Sc'),
        ('M.Sc', 'M.Sc'),
        ('B.Com', 'B.Com'),
        ('B.A', 'B.A'),
        ('M.A', 'M.A'),
        ('M.B.A', 'M.B.A'),
    ]
    
    OS_REQUIRED=[
        ('', 'Select Your OS Required'),
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
    ]
    department_name = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    semester = forms.ChoiceField(choices=SEMESTER_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    degree = forms.ChoiceField(choices=DEGREE_CHOICES)
    os_required = forms.ChoiceField(choices=OS_REQUIRED)
    software_required_version_opensource = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    software_required_version_license = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    remarks=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    
    class Meta:
        model = LabRequest
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(LabRequestForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        