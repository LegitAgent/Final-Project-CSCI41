from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Participant, Activity, ActivityBooking

# Create your views here.


class ActivityListView(ListView):
    # show ALL activities, regardless of whether the user has enlisted in them
    pass

class ActivityDetailView(DetailView):
    # show a particular activity and allow the user to enlist in it
    pass

class EnlistedActivityListView(ListView):
    # show the activities which the user has enlisted in
    pass
