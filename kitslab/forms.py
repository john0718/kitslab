from django import forms
from .models import Availability, LabDetails
from datetime import date
from .models import CredentialsManager

class AvailabilityForm(forms.ModelForm):
    SESSION_CHOICES = [
        ('Session-1', 'Session-1 [8 am to 11 am]'),
        ('Session-2', 'Session-2 [11 am to 2 pm]'),
        ('Session-3', 'Session-3 [2 pm to 5 pm]'),
    ]

    VENUE_CHOICES = [(str(i), f'Lab {i}') for i in range(1, 4)]

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select today or a future date'
    )
    session = forms.ChoiceField(choices=SESSION_CHOICES)
    lab_venue = forms.ChoiceField(choices=VENUE_CHOICES)

    lab_details = forms.ModelChoiceField(
        queryset=LabDetails.objects.all(),
        label="Lab Details",
        help_text="Select the lab session details (Course Code, Course Name, Batch)"
    )

    class Meta:
        model = Availability
        fields = ['lab_details', 'date', 'session', 'lab_venue']

    def clean_date(self):
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise forms.ValidationError("Please select today or a future date.")
        return selected_date



class CredentialsManagerForm(forms.ModelForm):
    class Meta:
        model = CredentialsManager
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ctc_faculty_name'].widget.attrs['readonly'] = True
        self.fields['ctc_faculty_mail_id'].widget.attrs['readonly'] = True
        self.fields['ctc_faculty_id'].widget.attrs.update({'id': 'faculty_id_dropdown', 'class': 'form-control'})



class ExcelUploadForm(forms.Form):
    file = forms.FileField()