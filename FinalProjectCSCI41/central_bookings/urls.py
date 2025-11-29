from django.urls import path
from .views import(
    index, ActivityListView, ActivityDetailView, ActivityUpdateView, ActivityDeleteView, activity_create, 
    enlist_in_activity, get_enlisted_activities_for_user
)

urlpatterns = [
    path('', index, name="index"),
    path('activities/', ActivityListView.as_view(), name='activity-list'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('activities/add/', activity_create, name='activity-add'),
    path('activities/<int:pk>/edit/', ActivityUpdateView.as_view(), name='activity-edit'),
    path('activities/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
    path('enlist/<int:activity_id>/', enlist_in_activity, name='enlist'),
    path('bookings/', get_enlisted_activities_for_user, name='bookings')
]

app_name = 'central_bookings'