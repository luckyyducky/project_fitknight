from django import forms
from .models import Group
from .models import GroupOrganiserProfile

class GroupForm(forms.ModelForm):
    group_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter group name'
        }),
        error_messages={
            'required': 'This field is required',
            'unique': 'A group with this name already exists'
        }
    )
    class Meta:
        model = Group
        fields = ['group_name', 'group_picture', 'description', 'activity_type', 'schedule', 'location']
        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'activity_type': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'schedule': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'location': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'group_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_activity_type(self):
        data = self.cleaned_data.get('activity_type', [])
        return ','.join(data) if data else ''

    def clean_schedule(self):
        data = self.cleaned_data.get('schedule', [])
        return ','.join(data) if data else ''

    def clean_location(self):
        data = self.cleaned_data.get('location', [])
        return ','.join(data) if data else ''   

class GroupOrganiserDetailsForm(forms.ModelForm):
    class Meta:
        model = GroupOrganiserProfile
        fields = ['about', 'milestones', 'group_organiser_picture', 'show_email', 'show_phone']
        widgets = {
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'milestones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'List your key achievements...'
            }),
            'group_organiser_picture': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'show_email': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_phone': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }

        
    