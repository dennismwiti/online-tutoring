# Generated by Django 5.0.1 on 2024-02-06 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_alter_degree_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='degree_teacher', to='teachers.teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree',
            field=models.ForeignKey(blank=True, choices=[('Bachelor of Education (B.Ed.)', 'Bachelor of Education (B.Ed.)'), ('Postgraduate Certificate in Education (PGCE)', 'Postgraduate Certificate in Education (PGCE)'), ('Bachelor of Arts (BA)', 'Bachelor of Arts (BA)'), ('Master of Education (M.Ed.)', 'Master of Education (M.Ed.):'), ('Continuing Professional Development (CPD)', 'Continuing Professional Development (CPD)')], null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_degree', to='teachers.degree'),
        ),
    ]
