from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserManager(BaseUserManager):
    def create_user(self, name, participant_type, department, birthdate, password=None):
        if not name:
            raise ValueError('Users must have a name')
        user = self.model(
            name=name,
            participant_type=participant_type,
            department=department,
            birthdate=birthdate
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, participant_type, department, birthdate, password):
        user = self.create_user(
            name=name,
            participant_type=participant_type,
            department=department,
            birthdate=birthdate,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin,BaseModel):

    PARTICIPANT_TYPES = {
        'Student': 'Student',
        'Faculty': 'Faculty',
        'Staff': 'Staff'
    }
    name = models.CharField(max_length=255, unique=True)
    participant_type = models.CharField(max_length=30,choices=PARTICIPANT_TYPES)
    department = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)        

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['participant_type', 'department', 'birthdate']

    objects = UserManager()

    def __str__(self):
        return self.name

