from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from .tasks import generate_and_assign_user_id, create_user_profile
from .choices_fields import Roles

# Create your models here.


class UserManager(BaseUserManager):
    def _create(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, username, password, **extra_fields):
        return self._create(username, password, **extra_fields)

    def create_supersuer(self, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self._create(username, password, **extra_fields)
    
    
class User(AbstractUser):
    id = models.CharField(primary_key=True, unique=True, max_length=10)
    username = models.CharField(max_length=150, unique=True, verbose_name="")
    email = models.EmailField(unique=True, blank=False, verbose_name="")
    phone_number = models.CharField(max_length=30, blank=False, null=True, verbose_name="")
    data_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=Roles.choices , default=Roles.ATTENDEE)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.role} - {self.username}"
        
        
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)

        if is_new:
            generate_and_assign_user_id.delay(self.pk, self.role)
            create_user_profile.delay(self.id)
    