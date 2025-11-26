from django.urls import path
from .views import(
    ActivityListView, ActivityDetailView, EnlistedActivityListView, enlist_in_activity
)

urlpatterns = [
    path('activities/', ActivityListView.as_view(), name='activities-list'),
    path('activities/activity/<int:pk>', ActivityDetailView.as_view(), name='activity'),
    path('enlist/<int:activity_id>/', enlist_in_activity, name='enlist')
]

app_name = 'central_bookings'