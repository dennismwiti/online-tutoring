# Generated by Django 5.0.1 on 2024-01-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_facebook_url_teacher_google_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image_url',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
