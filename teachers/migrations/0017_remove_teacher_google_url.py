# Generated by Django 4.2.7 on 2024-02-16 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0016_teacher_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='google_url',
        ),
    ]
