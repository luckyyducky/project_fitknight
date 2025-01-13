from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def home_view(request):
    return render(request, 'accounts/home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home_view, name='home'),
    path('buddy_portal/', include('buddy_portal.urls')),
    path('group_portal/', include('group_portal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
