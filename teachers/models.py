from django.db import models


class Teacher(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    DEPARTMENT_CHOICES = (
        ('math', 'Mathematics'),
        ('science', 'Science'),
        ('english', 'English'),
        # Add more departments as needed
    )

    DEGREE_CHOICES = (
        ('Bachelor of Education (B.Ed.)', 'Bachelor of Education (B.Ed.)'),
        ('Postgraduate Certificate in Education (PGCE)', 'Postgraduate Certificate in Education (PGCE)'),
        ('Bachelor of Arts (BA)', 'Bachelor of Arts (BA)'),
        ('Master of Education (M.Ed.)', 'Master of Education (M.Ed.):'),
        ('Continuing Professional Development (CPD)', 'Continuing Professional Development (CPD)'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    position = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    image_url = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # Image field for teacher profile picture
    profile_picture = models.ImageField(upload_to='teacher_profiles/', blank=True, null=True)
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True)
    # Social media URLs
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
