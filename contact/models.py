from django.db import models
from datetime import datetime

# Create your models here.


class ContactMessage(models.Model):
				name = models.CharField(max_length=100)
				email = models.EmailField()
				subject = models.CharField(max_length=255)
				phone = models.CharField(max_length=200)
				message = models.TextField(blank=True)
				timestamp = models.DateTimeField(blank=True, default=datetime.now)

				def __str__(self):
								return f"{self.subject} - {self.name}"
