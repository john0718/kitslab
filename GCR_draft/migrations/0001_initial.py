# Generated by Django 5.2 on 2025-06-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.PositiveIntegerField(verbose_name='S. No')),
                ('school', models.CharField(choices=[('SET', 'School of Engineering and Technology'), ('SCST', 'School of Computer Science and Technology'), ('SAMM', 'School of Sciences Arts Media and Management'), ('SABS', 'School of Agriculture and Bio Sciences')], max_length=10)),
                ('division', models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('Agriculture', 'Agriculture'), ('Bioinformatics', 'Bioinformatics'), ('Biotechnology', 'Biotechnology'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Commerce', 'Commerce'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Artificial Intelligence and Machine Learning', 'Artificial Intelligence and Machine Learning'), ('Data Science and Cyber Security', 'Data Science and Cyber Security'), ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Robotics', 'Robotics'), ('Biomedical Engineering', 'Biomedical Engineering'), ('English', 'English'), ('Food Processing', 'Food Processing'), ('Information Technology', 'Information Technology'), ('Management Studies', 'Management Studies'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Media and Communication', 'Media and Communication'), ('Nano Sciences', 'Nano Sciences'), ('Physics', 'Physics'), ('Value Education', 'Value Education'), ('Water Institute', 'Water Institute'), ('ISDF', 'ISDF'), ('Computer Application', 'Computer Application'), ('Criminology', 'Criminology'), ('Digital Sciences', 'Digital Sciences'), ('Data Science and Analytics', 'Data Science and Analytics'), ('Clinical Psychology', 'Clinical Psychology'), ('Others', 'Others')], max_length=50)),
                ('year', models.CharField(choices=[('I', 'I year'), ('II', 'II year'), ('III', 'III year'), ('IV', 'IV year'), ('V', 'V year')], max_length=5)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2)),
                ('degree', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('B.Com', 'B.Com'), ('BCA', 'BCA'), ('B.Sc', 'B.Sc'), ('B.A', 'B.A'), ('M.A', 'M.A'), ('MBA', 'MBA'), ('M.Sc', 'M.Sc'), ('Research', 'Research'), ('Others', 'Others')], max_length=20)),
                ('branch', models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('Agriculture', 'Agriculture'), ('Bioinformatics', 'Bioinformatics'), ('Biotechnology', 'Biotechnology'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Commerce', 'Commerce'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Artificial Intelligence and Machine Learning', 'Artificial Intelligence and Machine Learning'), ('Data Science and Cyber Security', 'Data Science and Cyber Security'), ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Robotics', 'Robotics'), ('Biomedical Engineering', 'Biomedical Engineering'), ('English', 'English'), ('Food Processing', 'Food Processing'), ('Information Technology', 'Information Technology'), ('Management Studies', 'Management Studies'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Media and Communication', 'Media and Communication'), ('Nano Sciences', 'Nano Sciences'), ('Physics', 'Physics'), ('Value Education', 'Value Education'), ('Water Institute', 'Water Institute'), ('ISDF', 'ISDF'), ('Computer Application', 'Computer Application'), ('Criminology', 'Criminology'), ('Digital Sciences', 'Digital Sciences'), ('Data Science and Analytics', 'Data Science and Analytics'), ('Clinical Psychology', 'Clinical Psychology'), ('Others', 'Others')], max_length=50)),
                ('course_code', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=100)),
                ('credits', models.CharField(choices=[('0.5', '0.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('4', '4'), ('Others', 'Others')], max_length=10)),
                ('batch_no', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=2)),
                ('course_type', models.CharField(choices=[('Theory', 'Theory'), ('Practical', 'Practical'), ('Placement', 'Placement')], max_length=20)),
                ('mode', models.CharField(choices=[('offline', 'Offline'), ('blended', 'Blended')], max_length=10)),
                ('faculty_id', models.CharField(max_length=20)),
                ('faculty_name', models.CharField(max_length=100)),
                ('faculty_contact_number', models.CharField(max_length=15)),
                ('faculty_email', models.EmailField(max_length=254)),
                ('timetable', models.TextField(help_text='Format: Day-Hour')),
            ],
        ),
    ]
