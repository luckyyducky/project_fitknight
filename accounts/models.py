from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_buddy_finder = models.BooleanField(default=False)
    is_group_organizer = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="custom_user_groups",
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name="custom_user"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custom_user_permissions",
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name="custom_user"
    )

    def __str__(self):
        return self.username
    
