from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from .forms import ActivityForm
from .models import Activity, ActivityBooking, Reservation

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ActivityListView(ListView):
    """Activity list view for activities."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (hasattr(self.request.user, 'organizer')):
            context["user_type"] = 'organizer'
        else:
            my_bookings = ActivityBooking.objects.filter(
                participant=self.request.user.participant)
            my_bookings = [booking.activity.pk for booking in my_bookings]
            print(my_bookings)
            context["user_type"] = 'participant'
            context["my_bookings"] = my_bookings
        

        return context
    
    model = Reservation
    template_name = 'activity_list.html'

class ActivityDetailView(DetailView):
    """Activity detail view for activities."""
    
    model = Activity
    template_name = 'activity_detail.html'

@login_required
def activity_create(request):
    """Activity create view for activities."""

    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            activity = Activity()
            activity.name = request.POST.get("name")
            activity.organizer = request.user.organizer
            activity.expected_participants = request.POST.get("expected_participants")
            activity.save()

            return redirect('central_bookings:activity-list')
        else:
            print(form.errors.as_data())

    else:
        form = ActivityForm()

    ctx = {
        "form": form
    }

    return render(request, 'activity_add.html', ctx)
    

class ActivityUpdateView(UpdateView):
    """Activity update view for activities."""
    
    model = Activity
    form_class = ActivityForm
    template_name = 'activity_update.html'
    
class ActivityDeleteView(DeleteView):
    """Activity delete view for activities."""
    
    model = Activity
    template_name = 'activity_delete.html'
    success_url = reverse_lazy('central_bookings:activity-list') # from urls.py list

def enlist_in_activity(request, activity_id):
    """Retrieves the activity from the database and saves it as enlisted for the user's request."""
    
    activity = get_object_or_404(Activity, id=activity_id) # safer
    user = request.user.participant

    if request.method == 'POST':
        booking = ActivityBooking.objects.create(
            participant=user,
            activity=activity,
            attended = False
        )
        booking.save()
        return redirect('central_bookings:activity-list')
    
def get_enlisted_activities_for_user(request):
    """Gets all activies that the user is enlisted in, as well as all their reservations."""

    user = request.user.participant

    # prevents extra database queries when you later access r.location.name
    reservation_qs = Reservation.objects.select_related('location')
    
    bookings_qs = (
        ActivityBooking.objects
        .filter(participant=user)
        .select_related('participant', 'activity', 'activity__organizer') # avoids extra queries per booking.
        .prefetch_related(
            Prefetch(
                'activity__reservations',
                queryset=reservation_qs, to_attr='prefetched_reservations')
            ) 
        # prefetch reservations with locations for activities.
        # 1st args: fetch bookings 2nd args: fetch reservations related to activities in bookings.
        # 3rd args: store prefetched reservations in 'prefetched_reservations' attribute instead of .reservations.all().
    )

    # build a list of results (one item per reservation if multiple reservations).
    enlisted = []
    for booking in bookings_qs:
        activity = booking.activity
        organizer_name = activity.organizer.user.first_name
        user_name = booking.participant.user.first_name

        reservations = getattr(activity, 'prefetched_reservations', list(activity.reservations.all()))
        for r in reservations:
            # dictionary to hold details of each enlisted activity per reservation
            enlisted.append({
                'activity_name': activity.name,
                'user_name': user_name,
                'attended': booking.attended,
                'date': r.date,
                'start_time': r.start_time,
                'end_time': r.end_time,
                'location': r.location.name if r.location else None,
                'organizer': organizer_name,
                'activity_url': activity.get_absolute_url,
                'activity_pk': booking.pk
            })
        
        # If the user marks an activity as attended
        # update the model isntance accordingly. 
        if (request.method=="POST" and "attendance_check_button" in request.POST):
            attended_booking = ActivityBooking.objects.get(pk=int(request.POST.get('activity_pk')))
            attended_booking.mark_attended()
            attended_booking.save()
            return redirect(reverse('central_bookings:bookings'))

    ctx = {'enlisted_activities': enlisted, 'profile': user}
    return render(request, 'bookings_list.html', ctx)
    # return render(request, 'profile.html', ctx)
