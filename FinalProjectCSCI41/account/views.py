from django.shortcuts import render
from .models import User

# Create your views here.
def profile_view(request):
    user = request.user

    ctx = {'profile': user}
    return render(request, 'profile.html', ctx)
