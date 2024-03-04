from django.urls import path
from . import views


urlpatterns = [
				path('', views.courses, name='courses'),
				path('<int:id>', views.course_details, name='course-details'),
				path('search', views.search_courses, name='search_courses'),
				path('course/<str:category>', views.category_courses, name='course-list')
]
