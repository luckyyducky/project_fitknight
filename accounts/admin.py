from django.contrib import admin
from .models import User
from .models import BuddyProfile
from .models import GroupProfile

admin.site.register(User)
admin.site.register(BuddyProfile)

@admin.register(GroupProfile)
class GroupProfileAdmin(admin.ModelAdmin):
    fields = ('name', 'creator', 'activity_types', 'schedules', 'locations')  # Explicitly listing fields
    list_display = ('name', 'creator')

    def get_activity_types(self, obj):
        return ", ".join(obj.activity_types)
    get_activity_types.short_description = 'Activity Types'

    def get_schedules(self, obj):
        return ", ".join(obj.schedules)
    get_schedules.short_description = 'Schedules'

    def get_locations(self, obj):
        return ", ".join(obj.locations)
    get_locations.short_description = 'Locations'
