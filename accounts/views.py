from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.urls import reverse_lazy
from buddy_portal.models import BuddyProfile

def home(request):
    if request.user.is_authenticated:
        if request.user.is_buddy_finder:
            return redirect('buddy_finder')
        return redirect('group_organizer')
    return render(request, 'accounts/home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            if not user.profile_picture:
                user.profile_picture = 'profile_pics/default.png'  # Default picture

            user_type = form.cleaned_data.get('user_type')
            if user_type == 'buddy_finder':
                user.is_buddy_finder = True
            else:
                user.is_group_organizer = True
            user.save()
            
            # Create BuddyProfile immediately after signup for buddy_finder users
            if user.is_buddy_finder:
                BuddyProfile.objects.create(
                    user=user,
                    profile_picture='profile_pics/default.png',
                    contact_phone=form.cleaned_data.get('phone_number', ''),  # Adjust field names based on your form
                    contact_email=user.email,
                    show_phone=True,  # Default privacy settings
                    show_email=True,  
                )
            
            login(request, user)
            if user.is_buddy_finder:
                return redirect('buddy_finder_details')
            return redirect('group_portal:group_organiser_details')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        if self.request.user.is_buddy_finder:
            return reverse_lazy('buddy_finder_portal')
        return reverse_lazy('group_portal:group_dashboard')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
