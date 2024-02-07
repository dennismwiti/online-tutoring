from django.contrib import admin
from .models import Inquiry


# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'country', 'town', 'phone', 'subjects',
                    'requirements', 'create_date',)
    list_filter = ('email', 'phone', 'create_date',)
    search_fields = ('id', 'email', 'phone',)


admin.site.register(Inquiry, InquiryAdmin)
