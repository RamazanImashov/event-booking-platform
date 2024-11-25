from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from .tasks import generate_and_assign_user_id_celery
from users.utils.choices_fields import Roles

# Create your models here.


class UserManager(BaseUserManager):
    def _create(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        if not username:
            raise ValueError("The Username field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password, **extra_fields):
        return self._create(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", Roles.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create(email, username, password, **extra_fields)
    
    
class User(AbstractUser):
    custom_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, verbose_name="username")
    email = models.EmailField(unique=True, blank=False, verbose_name="email")
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name="Phone Number")
    created_ad = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.ATTENDEE, blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.custom_id} - {self.email} - {self.role} - {self.username}"

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)

        if is_new and not self.custom_id:
            generate_and_assign_user_id_celery.delay(self.pk, self.role)
