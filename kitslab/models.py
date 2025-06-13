from django.db import models

class LabDetails(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=10)

    faculty_id = models.CharField(max_length=20)
    faculty_name = models.CharField(max_length=100)

    asst_fac1_id = models.CharField(max_length=20, blank=True, null=True)
    asst_fac1_name = models.CharField(max_length=100, blank=True, null=True)

    asst_fac2_id = models.CharField(max_length=20, blank=True, null=True)
    asst_fac2_name = models.CharField(max_length=100, blank=True, null=True)

    ctc_lab_no = models.CharField(max_length=20)
    day = models.CharField(max_length=20)  
    hours = models.CharField(max_length=50)  

    ctc_fac_id = models.CharField(max_length=20)
    ctc_fac_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Lab details"
        unique_together = ('course_code', 'course_name', 'batch_no')

    def __str__(self):
        return f"{self.course_code} - {self.course_name} - Batch {self.batch_no}"
        


class StudentsDetails(models.Model):
    student_regno = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)

    lab_details = models.ForeignKey(
        LabDetails,
        on_delete=models.CASCADE,
        related_name='students',
        null=True,  
        blank=True
    )

    def __str__(self):
        return f"{self.student_name} ({self.student_regno})"
    
    class Meta: 
        verbose_name_plural = "Student details"





class Availability(models.Model):
    lab_details = models.ForeignKey(
        LabDetails,
        on_delete=models.CASCADE,
        related_name='availabilities',
        null=True,  
        blank=True
    )
    date = models.DateField()
    session = models.CharField(max_length=20)
    lab_venue = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    student_strength = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.lab_details:
            self.student_strength = self.lab_details.students.count()
        else:
            self.student_strength = 0
        super().save(*args, **kwargs)

    def __str__(self):
        if self.lab_details:
            return f"{self.lab_details.course_code} - {self.date} ({self.session})"
        return f"Unknown Lab - {self.date} ({self.session})"

    class Meta:
        verbose_name_plural = "Availabilities"


    



class ExamAllocation(models.Model):
    lab_details = models.ForeignKey(
        LabDetails,
        on_delete=models.CASCADE,
        related_name='exam_allocations',
        null=True,  
        blank=True
    )
    date = models.DateField()
    session = models.CharField(max_length=20)
    lab_venue = models.CharField(max_length=50)
    student_strength = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.lab_details:
            self.student_strength = self.lab_details.students.count()
        else:
            self.student_strength = 0
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Exam Allocation"

    def __str__(self):
        return f"{self.lab_details} - {self.date} - {self.session}"




class CredentialsManager(models.Model):
    session_no=models.CharField(max_length=30,null=True,blank=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=20)
    date = models.DateField()
    student_strength = models.IntegerField(null=True, blank=True) 
    session = models.CharField(max_length=50)
    lab_venue = models.CharField(max_length=50)
    ctc_faculty_id = models.CharField(max_length=20)
    ctc_faculty_name = models.CharField(max_length=100)
    ctc_faculty_mail_id = models.EmailField()
    last_generated = models.DateTimeField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Credentials Manager"

    def __str__(self):
        return f"Staff Name: {self.ctc_faculty_name}-{self.course_code} - Batch {self.batch_no} - {self.date} {self.session}"
 

class GeneratedCredential(models.Model):
    session_no=models.CharField(max_length=30,null=True,blank=True)
    course_code = models.CharField(max_length=20,null=True, blank=True)
    course_name = models.CharField(max_length=100,null=True, blank=True)
    batch_no = models.CharField(max_length=20,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    session = models.CharField(max_length=30,null=True, blank=True)
    lab_venue = models.CharField(max_length=50,null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    regno = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username}-{self.password}-{self.course_code} - Batch {self.batch_no} - {self.date} {self.session}"
    



class AssignedCourses(models.Model):
    department_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)
    numberofcredits = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=200)
    num_slots = models.CharField(max_length=100)
    num_batches = models.CharField(max_length=100,blank=True, null=True)
    os_required = models.CharField(max_length=500,blank=True, null=True)
    software_required_version_opensource = models.CharField(max_length=500,blank=True, null=True)
    software_required_version_license = models.CharField(max_length=500,blank=True, null=True)
    remarks = models.CharField(blank=True, null=True)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assigned: {self.course_code} on {self.assigned_date.strftime('%d-%m-%Y')}"
