# Generated by Django 5.0.1 on 2024-01-26 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_remove_course_prerequisites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='assessment_methods',
        ),
        migrations.RemoveField(
            model_name='course',
            name='grading_scale',
        ),
    ]