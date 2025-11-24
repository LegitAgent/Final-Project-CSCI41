from django.db import models
from django.urls import reverse

# Create your models here.

class Organizer(models.Model):
    
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
        return self.name
    
    class Meta:
        verbose_name = 'Organizer'

class Activity(models.Model):

    name = models.CharField(max_length=255)
    expected_participants = models.IntegerField

    organizer = models.ForeignKey(Organizer,
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  related_name='activities')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('central_bookings:activity', args=[str(self.pk)])
    
    def get_reservations(self):
        return self.reservations.all()

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

class Participant(models.Model):
    
    PARTICIPANT_TYPES = {
        'Student': 'Student',
        'Faculty': 'Faculty',
        'Staff': 'Staff'
    }

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    participant_type = models.CharField(choices=PARTICIPANT_TYPES)
    department = models.CharField(max_length=255)
    birthdate = models.DateTimeField(default='2000-0-0 00:00:00')

    class Meta:
        verbose_name = 'Participant'

class ActivityBooking(models.Model):

    activity = models.ForeignKey(Activity,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 related_name='activity_bookings')
    participant = models.ForeignKey(Participant,
                                    null=False, 
                                    on_delete=models.CASCADE,
                                    related_name='activity_bookings')
    attended = models.BooleanField(default=False)

    # i realized idk if participant should be a Participant or Profile...

    class Meta:
        verbose_name = 'Activity Booking'

class Location(models.Model):
    
    name = models.CharField(max_length=255)
    maximum_capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location'

class Reservation(models.Model):

    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    location = models.ForeignKey(Location,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 )
    
    activity = models.ForeignKey(Activity,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 related_name='reservations')

    def __str__(self):
        return self.activity.name + " happening in " + self.location.name + " from " + str(self.start_time) + " to " + str(self.end_time)

    class Meta:
        verbose_name = 'Reservation'
    
