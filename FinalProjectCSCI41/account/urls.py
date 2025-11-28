from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from central_bookings.views import get_enlisted_activities_for_user

urlpatterns = [
    path('profile/', get_enlisted_activities_for_user, name='profile'),
]

app_name = 'account'