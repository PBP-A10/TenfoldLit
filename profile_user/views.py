from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse

@login_required
def get_user_data(request):
    user = request.user
    user_data = {
        "name": user.username,
        "email": user.email,
        "username": user.username,  # Add the username field
    }
    return JsonResponse(user_data)

@login_required
def update_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        profile_picture = request.FILES.get('profile-picture')
        
        user = request.user
        user.username = username
        if profile_picture:
            user.profile_picture = profile_picture
        user.save()
        
    return render(request, 'profile.html')
