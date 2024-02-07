# Generated by Django 5.0.1 on 2024-01-25 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_alter_course_teacher_alter_degree_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_degree', to='teachers.degree'),
        ),
    ]