from django.contrib import admin
from .models import User 
from .models import BuddyProfile
from .models import GroupProfile

admin.site.register(User)
admin.site.register(BuddyProfile)
admin.site.register(GroupProfile)