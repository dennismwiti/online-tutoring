# Generated by Django 5.0.1 on 2024-02-07 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_is_related'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='is_related',
        ),
    ]
