from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField 
import json


class User(AbstractUser):
    is_buddy_finder = models.BooleanField(default=False)
    is_group_organizer = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_groups",
        related_query_name="custom_user"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="custom_user"
    )

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fitness_goals = MultiSelectField(choices=FITNESS_GOALS_CHOICES,max_choices=5, blank=True)
    workout_preferences = MultiSelectField(choices=WORKOUT_PREFERENCES_CHOICES, max_choices=5, blank=True)
    availability = MultiSelectField(choices=AVAILABILITY_CHOICES, max_choices=4, blank=True)

    def __str__(self):
        return f"Buddy Profile of: {self.user.username}"

class GroupProfile(models.Model):
    ACTIVITY_TYPES = [
        ('Cardio', 'Cardio'),
        ('Strength Training', 'Strength Training'),
        ('Meditation', 'Meditation'),
        ('Team Sports', 'Team Sports'),
    ]
    
    SCHEDULES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Biweekly', 'Biweekly'),
    ]

    LOCATIONS = [
        ('Gym A', 'Gym A'),
        ('Gym B', 'Gym B'),
        ('Park', 'Park'),
        ('Community Center', 'Community Center'),
    ]

    creator = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    activity_types = MultiSelectField(choices=ACTIVITY_TYPES, max_choices=4, blank=True)
    schedules = MultiSelectField(choices=SCHEDULES , max_choices=3, blank=True)
    locations = MultiSelectField(choices=LOCATIONS, max_choices=4, blank=True)

    
    def __str__(self):
        return f"Group Organizer Profile of: {self.creator.username}"
