from django.urls import path
from . import views

urlpatterns = [
				path('', views.teachers, name='teachers'),
				path('<int:id>', views.teachers_detail, name='teachers_detail'),
				path('search/', views.teachers_search, name='teachers_search'),
]
