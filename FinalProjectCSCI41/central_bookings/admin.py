from django.db import models
from django.contrib import admin

from .models import Organizer, Activity, Participant, ActivityBooking, Location, Reservation

# set up the in-lines

class ActivityInLine(admin.TabularInline):
    model = Activity

class ActivityBookingInLine(admin.TabularInline):
    model = ActivityBooking

class LocationInLine(admin.TabularInline):
    model = Location

class ReservationInLine(admin.TabularInline):
    model = Reservation

# set up the actual admins

class OrganizerAdmin(admin.ModelAdmin):
    model = Organizer
    inlines = [ActivityInLine]

class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    inlines = [ReservationInLine]

class ParticipantAdmin(admin.ModelAdmin):
    model = Participant

class LocationAdmin(admin.ModelAdmin):
    model = Location
    inlines = [ReservationInLine]

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Reservation, ReservationAdmin)