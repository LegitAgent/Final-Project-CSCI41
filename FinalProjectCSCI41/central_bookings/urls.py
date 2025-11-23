from django.urls import path
from .views import(
    ActivityListView, ActivityDetailView, EnlistedActivityListView
)

urlpatterns = [
    path('activities/', ActivityListView.as_view(), name='activities-list'),
    path('activities/activity/<int:pk>', ActivityDetailView.as_view(), name='activity')
]

app_name = 'central_bookings'