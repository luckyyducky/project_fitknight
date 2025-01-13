from django.shortcuts import render, redirect
from .forms import BuddyProfileForm
from django.contrib.auth.decorators import login_required
from .models import BuddyProfile
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.contrib.auth import get_user_model
import ssl
import certifi

ssl._create_default_https_context = ssl.create_default_context
ssl.get_default_verify_paths = lambda: certifi.where()

User = get_user_model()

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('my_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'buddy_portal/change_password.html', {'form': form})
    
@login_required
def buddy_finder_details(request):
    profile, created = BuddyProfile.objects.get_or_create(
        user=request.user,
        defaults={'profile_picture': 'profile_pics/default.png'}
    )  # Avoid creating a new profile unintentionally
    
    if request.method == 'POST':
        form = BuddyProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('buddy_finder_portal')
        else:
            messages.error(request, "Error updating profile")
    else:
        form = BuddyProfileForm(instance=profile)

    return render(request, 'buddy_portal/buddy_finder_details.html', {'form': form})

@login_required
def buddy_finder_portal(request):
    # Fetch all buddy profiles except the logged-in user's profile
    buddy_profiles = BuddyProfile.objects.exclude(user=request.user)

    return render(request, 'buddy_portal/buddy_finder_portal.html', {'buddy_profiles': buddy_profiles})

@login_required
def my_profile(request):
    profile, created = BuddyProfile.objects.get_or_create(
        user=request.user,
        defaults={'profile_picture': 'profile_pics/default.png'}
    )
    
    if request.method == "POST":
        form = BuddyProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('buddy_finder_portal')
    else:
        form = BuddyProfileForm(instance=profile)
    
    return render(request, 'buddy_portal/my_profile.html', {
        'form': form,
        'profile': profile
    })
