"""
URL configuration for onlinetutor project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('teachers/', include('teachers.urls')),
    path('course/', include('course.urls')),
    path('inquiry/', include('inquiry.urls')),
    path('contact/', include('contact.urls')),
    path('terms-and-conditions/', TemplateView.as_view(template_name='information/terms-and-conditions.html'),
         name='terms-and-conditions'),
    path('privacy-policy/', TemplateView.as_view(template_name='information/privacy-policy.html'),
         name='privacy-policy'),
    path('faqs/', TemplateView.as_view(template_name='information/faqs.html'),
         name='faqs'),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
