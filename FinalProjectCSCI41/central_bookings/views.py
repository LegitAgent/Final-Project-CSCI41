from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db import connection
from django.db.models import Prefetch

from .models import Activity, ActivityBooking, Reservation

# Create your views here.


class ActivityListView(ListView):
    # show ALL activities, regardless of whether the user has enlisted in them

    model = Activity
    template_name = 'activitiesList.html'

class ActivityDetailView(DetailView):
    # show a particular activity and allow the user to enlist in it

    model = Activity
    template_name = 'activityDetail.html'

class EnlistedActivityListView(ListView):
    # show the activities which the user has enlisted in
    
    pass

    model = ActivityBooking

    # need to do a little bit of logic here
    # to ensure that only the user's enlisted activities show up

def enlist_in_activity(request, activity_id):
    # logic to enlist the user in the activity with id=activity_id

    activity = Activity.objects.get(id=activity_id)
    user = request.user

    if request.method == 'POST':
        booking = ActivityBooking.objects.create(
            participant=user,
            activity=activity,
            attended = False
        )
        booking.save()
        return redirect('central_bookings:activities-list')
    
def get_enlisted_activities_for_user(request):
    user = request.user

    # prefetch reservations with their locations to avoid extra queries.
    #seperate querysets for booking and reservation to optimize queries 
    reservation_qs = Reservation.objects.select_related('location')
    bookings_qs = (
        ActivityBooking.objects
        .filter(participant=user)
        .select_related('participant', 'activity', 'activity__organizer') 
        #joins the tables for quick access to related fields
        .prefetch_related(Prefetch('activity__reservations', queryset=reservation_qs, to_attr='prefetched_reservations')) 
        # prefetch reservations with locations for activities
        # 1st args: fetch bookings 2nd args: fetch reservations related to activities in bookings 
        # 3rd args: store prefetched reservations in 'prefetched_reservations' attribute
    )

    # build a list of results (one item per reservation if multiple reservations)
    enlisted = []
    for booking in bookings_qs:
        activity = booking.activity
        organizer_name = activity.organizer.name 
        user_name = booking.participant.name

        reservations = getattr(activity, 'prefetched_reservations', list(activity.reservations.all()))
        for r in reservations:
            #dictionary to hold details of each enlisted activity per reservation
            #its like having internal ctx inside the ctx dictionary
            enlisted.append({
                'activity_name': activity.name,
                'user_name': user_name,
                'attended': booking.attended,
                'date': r.date,
                'start_time': r.start_time,
                'end_time': r.end_time,
                'location': r.location.name if r.location else None,
                'organizer': organizer_name,
            })

    ctx = {'enlisted_activities': enlisted, 'profile': user}
    return render(request, 'profile.html', ctx)


