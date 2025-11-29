from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import register_organizer, register_participant
from central_bookings.views import get_enlisted_activities_for_user

urlpatterns = [
    path('profile/', get_enlisted_activities_for_user, name='profile'),
    path('register/participant', register_participant, name='register_participant'),
    path('register/organizer', register_organizer, name='register_organizer'),
]

app_name = 'account'