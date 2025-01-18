from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'organizer', 'activity_type', 'schedule', 'location')
    search_fields = ('group_name', 'organizer__username')
    list_filter = ('activity_type', 'schedule', 'location')
