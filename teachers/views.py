from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.middleware.csrf import get_token
from .models import Teacher
from course.models import Course
from django.contrib import messages
# from django.views.decorators.cache import cache_page
# import hashlib


# Create your views here.
def teachers(request):
    all_teachers = Teacher.objects.all()
    paginator = Paginator(all_teachers, 6)
    page = request.GET.get('page', 1)

    try:
        paged_teachers = paginator.page(page)
    except PageNotAnInteger:
        paged_teachers = paginator.page(1)
    except EmptyPage:
        paged_teachers = paginator.page(paginator.num_pages)

    csrf_token = get_token(request)
    response = render(request, 'teachers/teachers.html', {'teachers': paged_teachers})
    response.set_cookie('csrftoken', csrf_token, httponly=True, samesite='Strict')
    return response


def teachers_detail(request, id, no_car=False):
    try:
        single_teacher = get_object_or_404(Teacher, pk=id)
        courses = Course.objects.filter(instructor=single_teacher)
        related_courses = courses.filter(is_related=True)
    except Teacher.DoesNotExist:
        single_teacher = None
        courses = None
        related_courses = None
    data = {
        'single_teacher': single_teacher,
        'courses': courses,
        'related_courses': related_courses,
    }
    return render(request, 'teachers/teacher-detail.html', data)


def teachers_search(request):
    subject = request.GET.get('subject', '')

    # Filter teachers based on the search query (case-insensitive)
    filtered_teachers = Teacher.objects.filter(department__icontains=subject)

    if not filtered_teachers:
        messages.warning(request, f"No tutor found for the subject '{subject}'.")

    # Pagination
    paginator = Paginator(filtered_teachers, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'teachers': page_obj,
        'query': subject,
    }

    return render(request, 'teachers/teachers.html', context)


#
# def get_style_hash():
#     style_content = "your_style_content_here"
#     return hashlib.sha256(style_content.encode('utf-8')).hexdigest()
