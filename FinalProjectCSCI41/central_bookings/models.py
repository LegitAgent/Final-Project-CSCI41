from django.db import models
from account.models import User
from django.urls import reverse

"""Provides the entities necessary for the database."""

class Organizer(models.Model):
    """A model that represents the Organizer Entity."""
    
    name = models.CharField(max_length=255)
    address = models.TextField()
    
    ORGANIZER_TYPES = {
        'Internal': 'Internal',
        'External': 'External'
    }
    organizer_type = models.CharField(choices=ORGANIZER_TYPES)

    contact_name = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=24)

    def __str__(self):
        """Returns the name of the model."""
        
        return self.name
    
    class Meta:
        """Metadata for the model."""
        
        verbose_name = 'Organizer'

class Participant(models.Model):
    """A model that represents the Participant Entity."""
    
    PARTICIPANT_TYPES = {
        'Student': 'Student',
        'Faculty': 'Faculty',
        'Staff': 'Staff'
    }

    def __str__(self):
        """Returns the name of the model."""
        
        return self.name

    name = models.CharField(max_length=255)
    participant_type = models.CharField(choices=PARTICIPANT_TYPES)
    department = models.CharField(max_length=255)
    birthdate = models.DateTimeField(default='2000-0-0 00:00:00')

    class Meta:
        """Metadata for the model"""
        
        verbose_name = 'Participant'

class Location(models.Model):
    """A model that represents the Location Entity."""
    
    name = models.CharField(max_length=255)
    maximum_capacity = models.IntegerField(default=1)

    def __str__(self):
        """Returns the name of the model."""
        
        return self.name

    class Meta:
        """Metadata for the model."""
        
        verbose_name = 'Location'

class Activity(models.Model):
    """A model that represents the Activity Entity."""
    
    name = models.CharField(max_length=255)
    expected_participants = models.IntegerField()

    organizer = models.ForeignKey(Organizer,
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  related_name='activities')
    
    location = models.ForeignKey(Location,
                                 null=False,
                                 on_delete=models.CASCADE)

    def __str__(self):
        """Returns the name of the model."""
        
        return self.name

    def get_absolute_url(self):
        """Returns the URL for the activity page."""
        
        return reverse('central_bookings:activity-detail', args=[str(self.pk)])
    
    def get_reservations(self):
        """Returns all reservation associated with the activity."""
        
        return self.reservations.all()

    class Meta:
        """Metadata for the model."""
        
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

class ActivityBooking(models.Model):
    """A model that represents the ActivityBooking Entity."""
    
    activity = models.ForeignKey(Activity,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 related_name='activity_bookings')
    participant = models.ForeignKey(User,
                                    null=False, 
                                    on_delete=models.CASCADE,
                                    related_name='activity_bookings')
    attended = models.BooleanField(default=False)

    class Meta:
        """Metadata for the model"""
        
        verbose_name = 'Activity Booking'


class Reservation(models.Model):
    """A model that represents the Reservation Entity."""
    
    date = models.DateField(null=False, default='2000-01-01')
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    location = models.ForeignKey(Location,
                                 null=False,
                                 on_delete=models.CASCADE)
    
    activity = models.ForeignKey(Activity,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 related_name='reservations')

    def __str__(self):
        """Returns how object is displayed in the admin panel."""
        
        return self.activity.name + " happening in " + self.location.name + " from " + str(self.start_time) + " to " + str(self.end_time)

    class Meta:
        """Metadata for the model."""
        
        verbose_name = 'Reservation'
    
