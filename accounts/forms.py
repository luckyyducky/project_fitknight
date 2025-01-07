from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from .models import BuddyProfile, GroupProfile
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    CHOICES = (
        ('buddy_finder', 'Buddy Finder'),
        ('group_organizer', 'Group Organizer'),
    )
    user_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect,
        label='User type'
    )
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'profile_picture', 'user_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove all help_text for username
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'
    
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class BuddyProfileForm(forms.ModelForm):
    class Meta:
        model = BuddyProfile
        fields = ['fitness_goals', 'workout_preferences', 'availability']
        widgets = {
              'fitness_goals': forms.TextInput(attrs={'class': 'form-control'}),
              'workout_preferences': forms.TextInput(attrs={'class': 'form-control'}),
              'availability': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GroupProfileForm(forms.ModelForm):
    class Meta:
        model = GroupProfile
        fields = ['activity_type', 'location', 'schedule']
        widgets = {
            'activity_type': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'schedule': forms.TextInput(attrs={'class': 'form-control'}),
       }