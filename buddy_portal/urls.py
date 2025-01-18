from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('my_profile/', views.my_profile, name='my_profile'),
    path('buddy_finder_details/', views.buddy_finder_details, name='buddy_finder_details'),
    path('buddy_finder_portal/', views.buddy_finder_portal, name='buddy_finder_portal'),
    path('change-password/', views.change_password, name='change_password'),
    path('profile/<int:pk>/', views.buddy_profile_view, name='buddy_profile'),
    path('group/<int:group_id>/join/', views.request_to_join, name='request_to_join'),
    path('group_profile/<int:pk>/', views.group_profile_view, name='group_profile'),
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='buddy_portal/password_reset.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='buddy_portal/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='buddy_portal/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='buddy_portal/password_reset_complete.html'), 
         name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
