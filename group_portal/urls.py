from django.urls import path
from . import views

app_name = 'group_portal'

urlpatterns = [
    path('dashboard/', views.group_dashboard, name='group_dashboard'),
    path('group_organiser_details/', views.group_organiser_details, name='group_organiser_details'),
    path('create_group/', views.create_group, name='create_group'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('organiser/profile/<int:user_id>/', views.view_group_organiser_profile, name='view_group_organiser_profile'),
    path('group/<int:group_id>/handle-request/<int:request_id>/', views.handle_join_request, name='handle_join_request'),
]
