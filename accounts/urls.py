from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('my-profile/', views.my_profile_view, name='my_profile'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('buddy-finder/', views.buddy_finder_portal, name='buddy_finder_portal'),
    path('group-organizer/', views.group_organizer_portal, name='group_organizer_portal'),
]