from django.db import models
from django.contrib import admin

from .models import Activity, ActivityBooking, Location, Reservation, Organizer, Participant

"""Putting all entities in the database as an inline for the admin"""

class ActivityInLine(admin.TabularInline):
    model = Activity
    extra = 1

class ActivityBookingInLine(admin.TabularInline):
    model = ActivityBooking
    extra = 1

class LocationInLine(admin.TabularInline):
    model = Location
    extra = 1

class ReservationInLine(admin.TabularInline):
    model = Reservation
    extra = 1

    
"""List all entities categorized by their corresponding models."""

class OrganizerAdmin(admin.ModelAdmin):
    model = Organizer
    inlines = [ActivityInLine]

class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    inlines = [ReservationInLine]

class ParticipantAdmin(admin.ModelAdmin):
    model = Participant

class ActivityBookingAdmin(admin.ModelAdmin):
    model = ActivityBooking

class LocationAdmin(admin.ModelAdmin):
    model = Location
    inlines = [ReservationInLine]

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation

"""Register all classes."""

admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityBooking, ActivityBookingAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Reservation, ReservationAdmin)