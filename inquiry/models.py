from django.db import models
from datetime import datetime
from django.core.validators import MaxLengthValidator, EmailValidator


# Create your models here.
class Inquiry(models.Model):

				Contact_time = (
								('anytime', 'Anytime'),
								('morning', 'Morning'),
								('afternoon', 'Afternoon'),
								('evening', 'Evening'),
				)

				Subjects = (
								('anytime', 'Anytime'),
								('morning', 'Morning'),
								('afternoon', 'Afternoon'),
								('evening', 'Evening'),
				)

				Tutoring_requirements = (
								('full time-instead of school', 'Full Time-Instead of School'),
								('full time-after schools and weekends', 'Full Time-After Schools and Weekends'),
								('full time-during school vacations', 'Full Time-During School Vacations'),
								('part time-15+ per week', 'Part Time-15+ Per Week'),
								('part time-less than 15 hours per week', 'Part Time-Less Than 15 Hours Per Week'),
				)
				Duration_time = (
								('anytime', 'Anytime'),
								('morning', 'Morning'),
								('afternoon', 'Afternoon'),
								('evening', 'Evening'),
				)

				fullname = models.CharField(max_length=300, validators=[MaxLengthValidator(300)])
				email = models.EmailField(max_length=300, validators=[EmailValidator(), MaxLengthValidator(300)])
				country = models.CharField(max_length=300, validators=[MaxLengthValidator(300)])
				town = models.CharField(max_length=300, validators=[MaxLengthValidator(300)])
				phone = models.CharField(max_length=20, blank=True, validators=[MaxLengthValidator(20)])
				contact_time = models.CharField(max_length=50, choices=Contact_time, validators=[MaxLengthValidator(50)])
				create_date = models.DateTimeField(default=datetime.now)
				subjects = models.CharField(choices=Subjects, max_length=15, validators=[MaxLengthValidator(15)])
				requirements = models.CharField(choices=Tutoring_requirements, max_length=400, validators=[MaxLengthValidator(400)])
				duration = models.CharField(choices=Duration_time, max_length=200, validators=[MaxLengthValidator(200)])

				def save(self, *args, **kwargs):
								super(Inquiry, self).save(*args, **kwargs)

				def __str__(self):
								return self.email
