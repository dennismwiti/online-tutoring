from django.contrib import admin
from .models import Teacher


# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
				class TeacherAdmin(admin.ModelAdmin):
								list_display = ['first_name', 'last_name', 'email', 'gender', 'department', 'position']
								search_fields = ['first_name', 'last_name', 'email']
								list_filter = ['gender', 'department', 'position']

				admin.site.register(Teacher, TeacherAdmin)
