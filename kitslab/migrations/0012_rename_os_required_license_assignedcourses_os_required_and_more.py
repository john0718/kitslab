# Generated by Django 5.2 on 2025-05-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitslab', '0011_alter_assignedcourses_num_slots_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignedcourses',
            old_name='os_required_license',
            new_name='os_required',
        ),
        migrations.RemoveField(
            model_name='assignedcourses',
            name='os_required_opensource',
        ),
        migrations.AddField(
            model_name='assignedcourses',
            name='num_batches',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
