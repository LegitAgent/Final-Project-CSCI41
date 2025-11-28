from django.shortcuts import render
from .models import User

def profile_view(request):
    """Renders the view for profile.html using the context user"""
    user = request.user

    ctx = {'profile': user}
    return render(request, 'profile.html', ctx)
