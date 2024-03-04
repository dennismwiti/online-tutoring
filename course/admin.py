from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'enrollment_status', 'status', 'visibility'
                    , 'is_related', 'category']
    search_fields = ['title', 'instructor__name']
    list_filter = ['enrollment_status', 'status', 'visibility']


admin.site.register(Course, CourseAdmin)
