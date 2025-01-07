from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .forms import BuddyProfileForm, GroupProfileForm
from .models import BuddyProfile, GroupProfile, User
from django.contrib.auth.decorators import login_required

@login_required
def buddy_finder_portal(request):
    buddy_profile = None
    try:
        buddy_profile = request.user.buddyprofile
        form = BuddyProfileForm(instance=buddy_profile)
    except BuddyProfile.DoesNotExist:
        form = BuddyProfileForm()

    if request.method == "POST":
        if 'switch_profile' in request.POST:
            # Save current buddy profile if it exists and has changes
            if buddy_profile and form.is_valid():
                form.save()
            
            request.user.is_buddy_finder = False
            request.user.is_group_organizer = True
            request.user.save()
            
            # Create or get group profile before redirecting
            GroupProfile.objects.get_or_create(user=request.user)
            return redirect('group_organizer_portal')
        
        form = BuddyProfileForm(request.POST, instance=buddy_profile) if buddy_profile else BuddyProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            # Ensure user type is set correctly when saving profile
            request.user.is_buddy_finder = True
            request.user.is_group_organizer = False
            request.user.save()
            
            messages.success(request, 'Buddy profile updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Buddy profile update Failed!')   
    return render(request, 'accounts/buddy_finder_portal.html', {'form': form})

@login_required
def group_organizer_portal(request):
    group_profile = None
    try:
        group_profile = request.user.groupprofile
        form = GroupProfileForm(instance=group_profile)
    except GroupProfile.DoesNotExist:
        form = GroupProfileForm()

    if request.method == "POST":
        if 'switch_profile' in request.POST:
            # Save current group profile if it exists and has changes
            if group_profile and form.is_valid():
                form.save()
            
            request.user.is_group_organizer = False
            request.user.is_buddy_finder = True
            request.user.save()
            
            # Create or get buddy profile before redirecting
            BuddyProfile.objects.get_or_create(user=request.user)
            return redirect('buddy_finder_portal')

        if 'fill_later' in request.POST:
            return redirect('home')
            
        form = GroupProfileForm(request.POST, instance=group_profile) if group_profile else GroupProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            # Ensure user type is set correctly when saving profile
            request.user.is_group_organizer = True
            request.user.is_buddy_finder = False
            request.user.save()
            
            messages.success(request, 'Group Profile updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Group profile update Failed!')        
    return render(request, 'accounts/group_organizer_portal.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user_type = form.cleaned_data['user_type']
                
                if user_type == 'buddy_finder':
                    user.is_buddy_finder = True
                    user.is_group_organizer = False
                else:
                    user.is_group_organizer = True
                    user.is_buddy_finder = False
                
                user.save()
                
                # Create the appropriate profile
                if user.is_buddy_finder:
                    BuddyProfile.objects.create(user=user)
                else:
                    GroupProfile.objects.create(user=user)
                
                raw_password = form.cleaned_data.get('password1')
                authenticated_user = authenticate(username=user.username, password=raw_password)
                
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    messages.success(request, 'Signup successful!')
                    return redirect('buddy_finder_portal' if user.is_buddy_finder else 'group_organizer_portal')
                else:
                    messages.error(request, "Authentication failed after signup.")
            except Exception as e:
                messages.error(request, f"An error occurred during signup: {str(e)}")
        else:
            messages.error(request, "Signup failed. Please check the form and try again.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully')
            
            # Direct to the appropriate portal based on active profile type
            if user.is_buddy_finder:
                return redirect('buddy_finder_portal')
            elif user.is_group_organizer:
                return redirect('group_organizer_portal')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def home_view(request):
    return render(request, 'accounts/home.html')

@login_required
def edit_profile(request):
    buddy_profile = None
    group_profile = None
    current_form = None
    
    if request.user.is_buddy_finder:
        try:
            buddy_profile = request.user.buddyprofile
            current_form = BuddyProfileForm(instance=buddy_profile)
        except BuddyProfile.DoesNotExist:
            current_form = BuddyProfileForm()
    elif request.user.is_group_organizer:
        try:
            group_profile = request.user.groupprofile
            current_form = GroupProfileForm(instance=group_profile)
        except GroupProfile.DoesNotExist:
            current_form = GroupProfileForm()

    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == 'switch_to_buddy':
            request.user.is_buddy_finder = True
            request.user.is_group_organizer = False
            request.user.save()
            BuddyProfile.objects.get_or_create(user=request.user)
            messages.success(request, 'Switched to Buddy Finder')
            return redirect('buddy_finder_portal')
            
        elif action == 'switch_to_organizer':
            request.user.is_buddy_finder = False
            request.user.is_group_organizer = True
            request.user.save()
            GroupProfile.objects.get_or_create(user=request.user)
            messages.success(request, 'Switched to Group Organizer')
            return redirect('group_organizer_portal')
            
        elif action == 'update_profile':
            if request.user.is_buddy_finder:
                form = BuddyProfileForm(request.POST, instance=buddy_profile)
            else:
                form = GroupProfileForm(request.POST, instance=group_profile)
                
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('edit_profile')
            else:
                messages.error(request, 'Profile update failed!')
                current_form = form

    return render(request, 'accounts/edit_profile.html', {
        'form': current_form,
        'is_buddy': request.user.is_buddy_finder,
        'is_organizer': request.user.is_group_organizer
    })

@login_required
def my_profile_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        # Handle profile switching
        if action == 'switch_to_buddy':
            request.user.is_buddy_finder = True
            request.user.is_group_organizer = False
            request.user.save()
            # Create buddy profile if it doesn't exist
            BuddyProfile.objects.get_or_create(user=request.user)
            messages.success(request, "Switched to Buddy Finder!")
            return redirect('buddy_finder_portal')
            
        elif action == 'switch_to_organizer':
            request.user.is_buddy_finder = False
            request.user.is_group_organizer = True
            request.user.save()
            # Create group profile if it doesn't exist
            GroupProfile.objects.get_or_create(user=request.user)
            messages.success(request, "Switched to Group Organizer!")
            return redirect('group_organizer_portal')

        # Handle profile updates
        if request.user.is_buddy_finder:
            try:
                profile = request.user.buddyprofile
                form = BuddyProfileForm(request.POST, instance=profile)
            except BuddyProfile.DoesNotExist:
                profile = None
                form = BuddyProfileForm(request.POST)
        else:
            try:
                profile = request.user.groupprofile
                form = GroupProfileForm(request.POST, instance=profile)
            except GroupProfile.DoesNotExist:
                profile = None
                form = GroupProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('my_profile')
        else:
            messages.error(request, "Please correct the errors below.")
    
    # GET request - display current profile
    else:
        if request.user.is_buddy_finder:
            try:
                profile = request.user.buddyprofile
                form = BuddyProfileForm(instance=profile)
            except BuddyProfile.DoesNotExist:
                form = BuddyProfileForm()
        else:
            try:
                profile = request.user.groupprofile
                form = GroupProfileForm(instance=profile)
            except GroupProfile.DoesNotExist:
                form = GroupProfileForm()

    return render(request, 'accounts/my_profile.html', {
        'form': form,
        'is_buddy': request.user.is_buddy_finder,
        'is_organizer': request.user.is_group_organizer
    })