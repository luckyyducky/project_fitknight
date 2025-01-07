from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fitness_goals = models.CharField(max_length=255, blank=True)
    workout_preferences = models.CharField(max_length=255, blank=True)
    availability = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Buddy Profile of: {self.user.username}"

class GroupProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    activity_type = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    schedule = models.CharField(max_length=255, blank=True)

    def __str__(self):
         return f"Group Profile of: {self.user.username}"