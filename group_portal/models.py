from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class Group(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('gym', 'Gym'),
        ('yoga', 'Yoga'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('dance', 'Dance'),
        ('aerobics', 'Aerobics'),
    ]

    SCHEDULE_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('weekends', 'Weekends'),
        ('weekday nights', 'Weekday Nights'),
    ]

    LOCATION_CHOICES = [
        ('park', 'Park'),
        ('gym', 'Gym'),
        ('community center', 'Community Center'),
        ('beach', 'Beach'),
        ('indoor', 'Indoor Facility'),
        ('outdoor', 'Outdoor Location'),
    ]

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_memberships', blank=True)
    group_name = models.CharField(max_length=100, default="Default Group Name", unique=True, blank=False)
    group_picture = models.ImageField(upload_to='group_pics/', blank=True, null=True)
    description = models.TextField(blank=False, null=True)
    activity_type = MultiSelectField(choices=ACTIVITY_TYPE_CHOICES, max_choices=3, blank=False)
    schedule = MultiSelectField(choices=SCHEDULE_CHOICES, max_choices=3, blank=False)
    location = MultiSelectField(choices=LOCATION_CHOICES, max_choices=3, blank=False)
    def __str__(self):
        return f"Group: {self.group_name} by {self.organizer.username}"

class GroupOrganiserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    group_organiser_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    milestones = models.TextField(null=True, blank=True)
    show_email = models.BooleanField(default=True)  # Add show_email field
    show_phone = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('group_request', 'New Group Join Request'),
        ('request_accepted', 'Group Join Request Accepted'),
        ('request_declined', 'Group Join Request Declined'),
    )

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    related_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='related_notifications', null=True)
    related_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']