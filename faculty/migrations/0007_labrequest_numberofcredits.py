# Generated by Django 5.2 on 2025-05-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0006_rename_os_required_license_labrequest_os_required_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labrequest',
            name='numberofcredits',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
