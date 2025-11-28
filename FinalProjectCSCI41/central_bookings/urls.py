from django.urls import path
from .views import(
    index, ActivityListView, ActivityDetailView, enlist_in_activity
)

urlpatterns = [
    path('', index, name="index"),
    path('activities/', ActivityListView.as_view(), name='activities-list'),
    path('activities/activity/<int:pk>', ActivityDetailView.as_view(), name='activity'),
    path('enlist/<int:activity_id>/', enlist_in_activity, name='enlist')
]

app_name = 'central_bookings'