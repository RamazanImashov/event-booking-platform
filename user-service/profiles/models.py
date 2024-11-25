from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_profile")
    permissions = models.TextField(blank=True, verbose_name="Права доступа")

    def __str__(self):
        return f"{self.user.custom_id} - {self.user.username} - {self.user.email}"


class OrganizerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizer_profile")
    organization_name = models.CharField(max_length=255, verbose_name="Название организации")
    is_verified = models.BooleanField(default=False, verbose_name="Организатор верифицирован")
    verified_documents = models.FileField(upload_to="organizer_docs/", blank=True, null=True, verbose_name="Документы для верификации")

    def __str__(self):
        return f"{self.user.custom_id} - {self.user.username} - {self.organization_name}"


class AttendeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="attendee_profile")
    preferences = models.JSONField(
        blank=True,
        null=True,
        verbose_name="Настройки",
        help_text="Настройки пользователя, связанные с уведомлениями, предпочтениями и т.д."
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.user.custom_id} - {self.user.username} - {self.user.email}"


class GuestProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="guest_profile")
    temp_id = models.CharField(max_length=50, unique=True, verbose_name="Временный ID")
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.custom_id} - {self.user.username} - {self.user.email}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'attendee':
            AttendeeProfile.objects.create(user=instance)
        elif instance.role == 'organizer':
            OrganizerProfile.objects.create(user=instance)
        elif instance.role == 'guest':
            GuestProfile.objects.create(user=instance)
        elif instance.role == 'admin':
            AdminProfile.objects.create(user=instance)

