from django.shortcuts import render, redirect
from teachers.models import Teacher
from course.models import Course
from django.contrib import messages


# Create your views here.
def home(request):
				all_courses = Course.objects.order_by('title')

				data = {
								'all_courses': all_courses,
				}
				return render(request, 'pages/home.html', data)


def about(request):
				teachers = Teacher.objects.all()
				data = {
								'teachers': teachers,
				}
				return render(request, 'pages/about-us.html', data)


def contact(request):
				if request.method == 'POST':
								name = request.POST['name']
								email = request.POST['email']
								subject = request.POST['subject']
								phone = request.POST['phone']
								message = request.POST['message']

								messages.success(request, 'Thank you for contacting us. We will get back to you shortly')

				return render(request, 'pages/contact-us.html')
