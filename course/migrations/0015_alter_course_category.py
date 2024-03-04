# Generated by Django 4.2.7 on 2024-02-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_remove_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(blank=True, choices=[('IGCSE', 'IGCSE'), ('GCSE', 'GCSE'), ('AS', 'AS'), ('IB', 'IB'), ('A-LEVELS', 'A-LEVELS'), ('O-LEVELS', 'O-LEVELS'), ('pre-University', 'pre-University'), ('Enhance-Exams', 'Enhance-Exams')], default=0, max_length=300),
        ),
    ]
