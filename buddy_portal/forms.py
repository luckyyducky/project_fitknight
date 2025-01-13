from django import forms
from .models import BuddyProfile

class BuddyProfileForm(forms.ModelForm):
    class Meta:
        model = BuddyProfile
        fields = ['profile_picture', 'about', 'fitness_goals', 'workout_preferences', 'availability',
                  'milestones', 'show_phone', 'show_email']
        widgets = {
            'fitness_goals': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'workout_preferences': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'availability': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'milestones': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
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
