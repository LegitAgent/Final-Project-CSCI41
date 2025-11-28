from django.urls import path
from .views import(
    index, ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView, enlist_in_activity
)

urlpatterns = [
    path('', index, name="index"),
    path('activities/', ActivityListView.as_view(), name='activity-list'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('activities/add/', ActivityCreateView.as_view(), name='activity-add'),
    path('activities/<int:pk>/edit/', ActivityUpdateView.as_view(), name='activity-edit'),
    path('activities/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
    path('enlist/<int:activity_id>/', enlist_in_activity, name='enlist')
]

app_name = 'central_bookings'