from django.db import models
from django.urls import reverse

# Create your models here.

class Organizer(models.Model):
    
    ORGANIZER_TYPES = {
        'Internal': 'Internal',
        'External': 'External'
    }

    name = models.CharField(max_length=255)
    address = models.TextField()
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

    def get_absolute_url(self):
        return reverse('ledger: recipe', args=[str(self.pk)])

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
    birthdate = models.DateTimeField

    class Meta:
        verbose_name = 'Participant'

class ActivityBooking(models.Model):

    activity = models.ForeignKey(Activity,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 related_name='activity_bookings')

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
    
    location = models.ForeignKey(Location,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 )
    
    activity = models.ForeignKey(Activity,
                                 null=False,
                                 on_delete=models.CASCADE,
                                 related_name='reservations')
    
    class Meta:
        verbose_name = 'Reservation'
    
