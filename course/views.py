from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.middleware.csrf import get_token
from django.views.decorators.cache import cache_page
from .models import Course
from django.db.models import Q
from django.db import connection


# Create your views here.
def courses(request):
				all_courses = Course.objects.order_by('title')
				paginator = Paginator(all_courses, 6)
				page = request.GET.get('page', 1)

				try:
								paged_courses = paginator.page(page)
				except PageNotAnInteger:
								paged_courses = paginator.page(1)
				except EmptyPage:
								paged_courses = paginator.page(paginator.num_pages)

				title_search = Course.objects.values_list('title', flat=True).distinct()
				instructor_search = Course.objects.values_list('instructor', flat=True).distinct()
				level_search = Course.objects.values_list('level', flat=True).distinct()

				category_choices = Course.objects.values_list('category', flat=True).distinct()

				search_title = request.GET.get('title', '')
				search_instructor = request.GET.get('instructor', '')
				search_level = request.GET.get('level', '')

				if search_title:
								paged_courses = paged_courses.filter(title__icontains=search_title)
				if search_instructor:
								paged_courses = paged_courses.filter(instructor__icontains=search_instructor)
				if search_level:
								paged_courses = paged_courses.filter(level__icontains=search_level)

				csrf_token = get_token(request)
				response = render(request, 'course/course-grid.html', {
								'courses': paged_courses,
								'title_search': title_search,
								'instructor_search': instructor_search,
								'level_search': level_search,
								'category_choices': category_choices,
								'search_title': search_title,
								'search_instructor': search_instructor,
								'search_level': search_level,
				})
				response.set_cookie('csrftoken', csrf_token, httponly=True, samesite='Strict')
				return response


def category_courses(request, category):

				filtered_courses = Course.objects.filter(category=category)

				course_per_page = 4

				paginator = Paginator(filtered_courses, course_per_page)
				page = request.GET.get('page', 1)

				try:
								paginated_courses = paginator.page(page)
				except PageNotInteger:
								paginated_courses = paginator.page(1)
				except EmptyPage:
								paginated_courses = paginator.page(paginator.num_pages)

				return render(request, 'course/course-list.html', {'filtered_courses': paginated_courses, 'category': category})


def course_details(request, id, no_course=False):
				try:
								single_course = get_object_or_404(Course, pk=id)
				except Course.DoesNotExist:
								single_course = None
				data = {
								'single_course': single_course,
				}
				return render(request, 'course/course-details.html', data)


@cache_page(60 * 15)
def search_courses(request):
				query = request.GET.get('q', '')
				category = request.GET.get('category', '')

				print("Query:", query)  # Print the value of the query parameter
				print("Category:", category)

				filtered_courses = Course.objects.all()

				if category:
								filtered_courses = filtered_courses.filter(category=category)
				else:
								filtered_courses = filtered_courses.filter(title__icontains=query)

				filtered_courses = filtered_courses.order_by('title')

				print("Filtered Courses Query:", filtered_courses.query)

				course_per_page = 4
				paginator = Paginator(filtered_courses, course_per_page)
				page = request.GET.get('page', 1)

				try:
								paginated_courses = paginator.page(page)
				except PageNotInteger:
								paginated_courses = paginator.page(1)
				except EmptyPage:
								paginated_courses = paginator.page(paginator.num_pages)

				return render(request, 'course/course-list.html', {'filtered_courses': paginated_courses, 'query': query, 'category': category})
