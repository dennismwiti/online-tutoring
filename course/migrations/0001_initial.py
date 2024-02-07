# Generated by Django 5.0.1 on 2024-01-20 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('days_and_time', models.CharField(max_length=255)),
                ('classroom', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
                ('enrollment_status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], max_length=20)),
                ('assessment_methods', models.TextField()),
                ('grading_scale', models.TextField()),
                ('textbooks', models.TextField()),
                ('additional_resources', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('undergraduate', 'Undergraduate'), ('graduate', 'Graduate')], max_length=20)),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived')], max_length=20)),
                ('visibility', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_images/')),
                ('prerequisites', models.ManyToManyField(blank=True, to='course.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.instructor')),
            ],
        ),
    ]
