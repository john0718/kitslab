from django.db import models

class CourseEntry(models.Model):
    SCHOOL_CHOICES = [
        ("SET", "School of Engineering and Technology"),
        ("SCST", "School of Computer Science and Technology"),
        ("SAMM", "School of Sciences Arts Media and Management"),
        ("SABS", "School of Agriculture and Bio Sciences"),
    ]

    YEAR_CHOICES = [
        ("I", "I year"), ("II", "II year"), ("III", "III year"),
        ("IV", "IV year"), ("V", "V year"),
    ]

    SEMESTER_CHOICES = [(str(i), f"{i}") for i in range(1, 11)]

    DEGREE_CHOICES = [
        ("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"), ("B.Com", "B.Com"),
        ("BCA", "BCA"), ("B.Sc", "B.Sc"), ("B.A", "B.A"),
        ("M.A", "M.A"), ("MBA", "MBA"), ("M.Sc", "M.Sc"),
        ("Research", "Research"), ("Others", "Others"),
    ]

    CREDITS_CHOICES = [
        ("0.5", "0.5"), ("1", "1"), ("1.5", "1.5"), ("2", "2"),
        ("2.5", "2.5"), ("3", "3"), ("4", "4"), ("Others", "Others"),
    ]

    BATCH_CHOICES = [(str(i), str(i)) for i in range(1, 21)]

    COURSE_TYPE_CHOICES = [
        ("Theory", "Theory"),
        ("Practical", "Practical"),
        ("Placement", "Placement"),
    ]

    MODE_CHOICES = [
        ("offline", "Offline"),
        ("blended", "Blended"),
    ]

    DIVISION_BRANCH_CHOICES = [
        ("Aerospace Engineering", "Aerospace Engineering"),
        ("Agriculture", "Agriculture"),
        ("Bioinformatics", "Bioinformatics"),
        ("Biotechnology", "Biotechnology"),
        ("Chemistry", "Chemistry"),
        ("Civil Engineering", "Civil Engineering"),
        ("Commerce", "Commerce"),
        ("Computer Science and Engineering", "Computer Science and Engineering"),
        ("Artificial Intelligence and Machine Learning", "Artificial Intelligence and Machine Learning"),
        ("Data Science and Cyber Security", "Data Science and Cyber Security"),
        ("Electrical and Electronics Engineering", "Electrical and Electronics Engineering"),
        ("Electronics and Communication Engineering", "Electronics and Communication Engineering"),
        ("Robotics", "Robotics"),
        ("Biomedical Engineering", "Biomedical Engineering"),
        ("English", "English"),
        ("Food Processing", "Food Processing"),
        ("Information Technology", "Information Technology"),
        ("Management Studies", "Management Studies"),
        ("Mathematics", "Mathematics"),
        ("Mechanical Engineering", "Mechanical Engineering"),
        ("Media and Communication", "Media and Communication"),
        ("Nano Sciences", "Nano Sciences"),
        ("Physics", "Physics"),
        ("Value Education", "Value Education"),
        ("Water Institute", "Water Institute"),
        ("ISDF", "ISDF"),
        ("Computer Application", "Computer Application"),
        ("Criminology", "Criminology"),
        ("Digital Sciences", "Digital Sciences"),
        ("Data Science and Analytics", "Data Science and Analytics"),
        ("Clinical Psychology", "Clinical Psychology"),
        ("Others", "Others"),
    ]

    
    school = models.CharField(max_length=10, choices=SCHOOL_CHOICES,null=True)
    division = models.CharField(max_length=50, choices=DIVISION_BRANCH_CHOICES,null=True)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES,null=True)
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES,null=True)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES,null=True)
    branch = models.CharField(max_length=50, choices=DIVISION_BRANCH_CHOICES,null=True)
    course_code = models.CharField(max_length=20,null=True)
    course_name = models.CharField(max_length=100,null=True)
    credits = models.CharField(max_length=10, choices=CREDITS_CHOICES,null=True)
    batch_no = models.CharField(max_length=2, choices=BATCH_CHOICES,null=True)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES,null=True)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES,null=True)
    faculty_id = models.CharField(max_length=20,null=True)
    faculty_name = models.CharField(max_length=100,null=True)
    faculty_contact_number = models.CharField(max_length=15,null=True)
    faculty_email = models.EmailField(null=True)
    timetable = models.TextField(help_text="Format: Day-Hour",null=True)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"
