from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile")
    permissions = models.TextField(blank=True, verbose_name="Права доступа")

class OrganizerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizer_profile")
    organization_name = models.CharField(max_length=255, verbose_name="Название организации")
    is_verified = models.BooleanField(default=False, verbose_name="Организатор верифицирован")
    verified_documents = models.FileField(upload_to="organizer_docs/", blank=True, null=True, verbose_name="Документы для верификации")

class AttendeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="attendee_profile")
    bookings = models.ManyToManyField("Event", through="Booking", verbose_name="Бронирования")
    notifications = models.ManyToManyField("Notification", blank=True, verbose_name="Уведомления")

class GuestProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="guest_profile")
    temp_id = models.CharField(max_length=50, unique=True, verbose_name="Временный ID")
    is_registered = models.BooleanField(default=False)
