from django import forms
from .models import BuddyProfile
from group_portal.models import Group

class BuddyProfileForm(forms.ModelForm):
    class Meta:
        model = BuddyProfile
        fields = ['profile_picture', 'about', 'fitness_goals', 'workout_preferences', 'availability',
                  'milestones','location','show_phone', 'show_email']
        widgets = {
            'fitness_goals': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'workout_preferences': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'availability': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'milestones': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'show_phone': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_email': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_fitness_goals(self):
        data = self.cleaned_data.get('fitness_goals', [])
        return ','.join(data) if data else ''

    def clean_workout_preferences(self):
        data = self.cleaned_data.get('workout_preferences', [])
        return ','.join(data) if data else ''

    def clean_availability(self):
        data = self.cleaned_data.get('availability', [])
        return ','.join(data) if data else ''
    
    def clean_location(self):
        data = self.cleaned_data.get('location', [])
        return ','.join(data) if data else ''
    
class BuddyFilterForm(forms.Form):
    fitness_goals = forms.MultipleChoiceField(
        choices=BuddyProfile.FITNESS_GOALS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    workout_preferences = forms.MultipleChoiceField(
        choices=BuddyProfile.WORKOUT_PREFERENCES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    availability = forms.MultipleChoiceField(
        choices=BuddyProfile.AVAILABILITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    location = forms.MultipleChoiceField(
        choices=BuddyProfile.LOCATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class GroupFilterForm(forms.Form):
    activity_type = forms.MultipleChoiceField(
        choices=Group.ACTIVITY_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    schedule = forms.MultipleChoiceField(
        choices=Group.SCHEDULE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    location = forms.MultipleChoiceField(
        choices=Group.LOCATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
