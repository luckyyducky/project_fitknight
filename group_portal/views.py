from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from buddy_portal.models import JoinRequest 
from .forms import GroupForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .forms import GroupOrganiserDetailsForm
from .models import GroupOrganiserProfile, Notification
from django.http import Http404

@login_required
def group_dashboard(request):
    groups = Group.objects.filter(organizer=request.user)
    unread_notifications = request.user.notifications.filter(is_read=False)
    for notification in unread_notifications:
        messages.info(request, notification.message)
        # Mark as read after showing
        notification.is_read = True
        notification.save()
    return render(request, 'group_portal/dashboard.html', {
        'groups': groups,
        'page_title': 'Group Organizer Dashboard'
    })

@login_required
def group_organiser_details(request):
    # Get or create the group organizer profile
    profile, created = GroupOrganiserProfile.objects.get_or_create(
        user=request.user,  # Use 'organizer' instead of 'user'
        defaults={'group_organiser_picture': 'profile_pics/default.png'}
    )
    
    if request.method == 'POST':
        form = GroupOrganiserDetailsForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('group_portal:group_dashboard')  # Redirect to group dashboard after saving
        else:
            messages.error(request, "Error updating profile")
    else:
        form = GroupOrganiserDetailsForm(instance=profile)

    return render(request, 'group_portal/group_organiser_details.html', {'form': form})

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                group = form.save(commit=False)
                group.organizer = request.user
                group.save()
                return redirect('group_portal:group_dashboard')
            except IntegrityError:
                form.add_error('group_name', 'A group with this name already exists. Please choose a different name.')
    else:
        form = GroupForm()
    return render(request, 'group_portal/create_group.html', {'form': form})

@login_required
def my_profile(request):
    try:
        profile = GroupOrganiserProfile.objects.get(user=request.user)
    except GroupOrganiserProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = GroupOrganiserDetailsForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('group_portal:group_dashboard')  # Redirect to profile page after updating
    else:
        form = GroupOrganiserDetailsForm(instance=profile)

    return render(request, 'group_portal/my_profile.html', {'form': form, 'profile': profile})

@login_required
def view_group_organiser_profile(request, user_id):
    try:
        profile = GroupOrganiserProfile.objects.get(user_id=user_id)
        return render(request, 'group_portal/view_group_organiser_profile.html', {
            'profile': profile
        })
    except GroupOrganiserProfile.DoesNotExist:
        raise Http404("Group organiser profile does not exist")
    
@login_required
def handle_join_request(request, group_id, request_id):
    if request.method == 'POST':
        group = get_object_or_404(Group, id=group_id, organizer=request.user)
        join_request = get_object_or_404(JoinRequest, id=request_id, group=group)

        action = request.POST.get('action')
        if action == 'accept':
            join_request.status = 'ACCEPTED'
            join_request.save()
            group.members.add(join_request.user)

            Notification.objects.create(
                recipient=join_request.user,
                notification_type='request_accepted',
                message=f'Your request to join {group.group_name} has been accepted!',
                related_user=request.user,
                related_group=group
            )
        elif action == 'decline':
            join_request.status = 'DECLINED'
            join_request.save()

            Notification.objects.create(
                recipient=join_request.user,
                notification_type='request_declined',
                message=f'Your request to join {group.group_name} was declined',
                related_user=request.user,
                related_group=group
            )
      
        return redirect('group_portal:group_detail', group_id=group_id)

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id, organizer=request.user)
    pending_requests = group.join_requests.filter(status='PENDING')
    members = group.members.all().order_by('username')

    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_portal:group_dashboard')
    else:
        form = GroupForm(instance=group)
    return render(request, 'group_portal/group_detail.html', {
        'group': group,
        'form': form,
        'pending_requests': pending_requests,
        'members': members
    })

