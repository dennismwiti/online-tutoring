from django.contrib import admin
from .models import ContactMessage


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
				list_display = ('id', 'name', 'email', 'subject', 'message', 'phone')
				list_display_links = ('id', 'name', 'email')
				search_fields = ('id', 'email')
				list_per_page = 12


admin.site.register(ContactMessage, ContactAdmin)

