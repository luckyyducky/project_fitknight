from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.conf import settings

class BuddyProfile(models.Model):
    FITNESS_GOALS_CHOICES = [
        ('Weight Loss', 'Weight Loss'),
        ('Muscle Gain', 'Muscle Gain'),
        ('General Fitness', 'General Fitness'),
        ('Cardio', 'Cardio'),
        ('Flexibility', 'Flexibility'),
    ]
    WORKOUT_PREFERENCES_CHOICES = [
        ('gym', 'Gym'),
        ('yoga', 'Yoga'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
    ]
    AVAILABILITY_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('weekends', 'Weekends'),
    ]

    LOCATION_CHOICES = [
        ('park', 'Park'),
        ('gym', 'Gym'),
        ('community center', 'Community Center'),
        ('beach', 'Beach'),
        ('indoor', 'Indoor Facility'),
        ('outdoor', 'Outdoor Location'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    fitness_goals = MultiSelectField(choices=FITNESS_GOALS_CHOICES, max_choices=5, blank=True)
    workout_preferences = MultiSelectField(choices=WORKOUT_PREFERENCES_CHOICES, max_choices=5, blank=True)
    availability = MultiSelectField(choices=AVAILABILITY_CHOICES, max_choices=4, blank=True)
    milestones = models.TextField(blank=True, help_text="Add key fitness milestones or achievements")
    location = MultiSelectField(choices=LOCATION_CHOICES, max_choices=6, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True, null=True)

    show_phone = models.BooleanField(default=True)
    show_email = models.BooleanField(default=True)

    def __str__(self):
        return f"Buddy Profile of: {self.user.username}"
    
class JoinRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='join_requests')
    group = models.ForeignKey('group_portal.Group', on_delete=models.CASCADE, related_name='join_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'group']
