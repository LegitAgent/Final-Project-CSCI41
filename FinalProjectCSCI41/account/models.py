from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Organizer(models.Model):
    """A model that represents the Organizer Entity."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

    ORGANIZER_TYPES = [
        ('Internal', 'Internal'),
        ('External', 'External'),
    ]

    organizer_type = models.CharField(max_length=20, choices=ORGANIZER_TYPES)
    contact_name = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=24)

    def __str__(self):
        """Returns the name of the model."""
        return self.user.first_name

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
        return self.user.first_name

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    participant_type = models.CharField(choices=PARTICIPANT_TYPES)
    department = models.CharField(max_length=255)
    birthdate = models.DateTimeField(default='2000-0-0 00:00:00')

    class Meta:
        """Metadata for the model"""
        verbose_name = 'Participant'


# class BaseModel(models.Model):
#     """Creates timestamps for all models who inherit it."""
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         """Metadata for the model."""
#         abstract = True

# class UserManager(BaseUserManager):
#     """Manages the creation of regular (normal) users and super (admin) users."""
#     def create_user(self, name, participant_type, department, birthdate, password=None):
#         """Creates and saves a regular user given the specific arguments."""
#         if not name:
#             raise ValueError('Users must have a name')
#         user = self.model(
#             name=name,
#             participant_type=participant_type,
#             department=department,
#             birthdate=birthdate
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, name, participant_type, department, birthdate, password):
#         """Creates and saves a super user given the specific arguments."""
#         user = self.create_user(
#             name=name,
#             participant_type=participant_type,
#             department=department,
#             birthdate=birthdate,
#             password=password
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.is_active = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin,BaseModel):
#     """Extends Django's user model by including additional fields like participant_types, department, birthdate, and etc."""
#     PARTICIPANT_TYPES = {
#         'Student': 'Student',
#         'Faculty': 'Faculty',
#         'Staff': 'Staff'
#     }
#     name = models.CharField(max_length=255, unique=True)
#     participant_type = models.CharField(max_length=30,choices=PARTICIPANT_TYPES)
#     department = models.CharField(max_length=255)
#     birthdate = models.DateField(null=True, blank=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)        

#     USERNAME_FIELD = 'name'
#     REQUIRED_FIELDS = ['participant_type', 'department', 'birthdate']

#     objects = UserManager() # attatch custom manager.

#     def __str__(self):
#         """Displays name in admin/shell."""
#         return self.name

