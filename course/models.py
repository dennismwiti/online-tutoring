from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Course(models.Model):

    DoesNotExist = None
    objects = None

    course_titles = (
        ('math', 'Mathematics'),
        ('science', 'Science'),
        ('english', 'English'),
        ('physics', 'Physics'),
        ('art', 'Art'),
        ('Chemistry', 'Chemistry'),
        ('History', 'History'),
        # Add more departments as needed
    )

    categories = (
        ('IGCSE', 'IGCSE'),
        ('GCSE', 'GCSE'),
        ('AS', 'AS'),
        ('IB', 'IB'),
        ('A-LEVELS', 'A-LEVELS'),
        ('O-LEVELS', 'O-LEVELS'),
        ('pre-University', 'pre-University'),
        ('Enhance-Exams', 'Enhance-Exams'),
    )

    title = models.CharField(max_length=255, choices=course_titles)
    description = RichTextField()
    category = models.CharField(choices=categories, max_length=300, blank=True, default=0)
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # start_date = models.DateField()
    # end_date = models.DateField()
    days_and_time = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    # classroom = models.CharField(max_length=50)
    # capacity = models.PositiveIntegerField()
    enrollment_status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])
    textbooks = models.TextField()
    additional_resources = models.TextField()
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=[('undergraduate', 'Undergraduate'), ('graduate', 'Graduate')])
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('archived', 'Archived')])
    visibility = models.BooleanField(default=True)
    is_related = models.BooleanField(default=False)
    # Add the image field
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    create_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
