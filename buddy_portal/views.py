from django.shortcuts import render, redirect, get_object_or_404
from .forms import BuddyProfileForm
from django.contrib.auth.decorators import login_required
from .models import BuddyProfile, JoinRequest
from group_portal.models import Group,Notification
from .forms import GroupFilterForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models.query_utils import Q
from django.contrib.auth import get_user_model
from .forms import BuddyFilterForm
from django.http import JsonResponse
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
    )
    
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
    buddy_profiles = BuddyProfile.objects.filter(user__is_buddy_finder=True).exclude(user=request.user)
    groups = Group.objects.all()
    active_tab = 'groups' if ('group_filter' in request.GET or request.GET.get('tab') == 'groups') else 'buddies'

    buddy_form = BuddyFilterForm(request.GET or None)
    if buddy_form.is_valid() and 'buddy_filter' in request.GET:
        fitness_goals = buddy_form.cleaned_data.get('fitness_goals')
        workout_preferences = buddy_form.cleaned_data.get('workout_preferences')
        availability = buddy_form.cleaned_data.get('availability')
        locations = buddy_form.cleaned_data.get('location')
        
        query = Q()
        if fitness_goals:
            for goal in fitness_goals:
                query |= Q(fitness_goals__icontains=goal)
        if workout_preferences:
            for preference in workout_preferences:
                query |= Q(workout_preferences__icontains=preference)
        if availability:
            for time in availability:
                query |= Q(availability__icontains=time)
        if locations:
            for location in locations:
                query |= Q(location__icontains=location)
        
        if query:
            buddy_profiles = buddy_profiles.filter(query)

    group_form = GroupFilterForm(request.GET or None)
    if group_form.is_valid() and 'group_filter' in request.GET:
        activity_types = group_form.cleaned_data.get('activity_type')
        schedules = group_form.cleaned_data.get('schedule')
        locations = group_form.cleaned_data.get('location')
        
        query = Q()
        if activity_types:
            for activity in activity_types:
                query |= Q(activity_type__icontains=activity)
        if schedules:
            for schedule in schedules:
                query |= Q(schedule__icontains=schedule)
        if locations:
            for location in locations:
                query |= Q(location__icontains=location)
        
        if query:
            groups = groups.filter(query)

    unread_notifications = request.user.notifications.filter(is_read=False)
    for notification in unread_notifications:
        messages.info(request, notification.message)
        notification.is_read = True
        notification.save()

    return render(request, 'buddy_portal/buddy_finder_portal.html', {
        'buddy_profiles': buddy_profiles,
        'groups': groups,
        'buddy_form': buddy_form,
        'group_form': group_form,
        'active_tab': active_tab,
    })

def buddy_profile_view(request, pk): 
    buddy_profile = get_object_or_404(BuddyProfile, pk=pk)
    context = {'buddy_profile': buddy_profile}
    return render(request, 'buddy_portal/buddy_profile.html', context)

def group_profile_view(request, pk):
    group_profile = get_object_or_404(Group, pk=pk)
    join_request = None
    if request.user.is_authenticated:
        join_request = JoinRequest.objects.filter(
            user=request.user,
            group=group_profile
        ).first()
    is_member = group_profile.members.filter(id=request.user.id).exists()
    can_access_chat = is_member or request.user == group_profile.organizer
    members = group_profile.members.all().order_by('username')
    
    context = {
        'group_profile': group_profile,
        'join_request': join_request,
        'is_member': is_member,
        'members': members,
        'can_access_chat': can_access_chat
    }
    return render(request, 'buddy_portal/group_profile.html', context)

@login_required
def request_to_join(request, group_id):
    if request.method == 'POST':
        group = get_object_or_404(Group, id=group_id)
        join_request, created = JoinRequest.objects.get_or_create(
            user=request.user,
            group=group,
            defaults={'status': 'PENDING'}
        )

        if created: 
            Notification.objects.create(
                recipient=group.organizer,
                notification_type='group_request',
                message=f'{request.user.username} has requested to join your group {group.group_name}',
                related_user=request.user,
                related_group=group
            )

        return redirect('group_profile', pk=group_id)



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
