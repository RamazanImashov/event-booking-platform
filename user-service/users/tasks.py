# users/tasks.py

from celery import shared_task
from django.contrib.auth import get_user_model
from utils import generate_user_id
from .profile_models import AdminProfile, OrganizerProfile, AttendeeProfile, GuestProfile

User = get_user_model()

@shared_task
def generate_and_assign_user_id(user_id: int, role: str):
    user = User.objects.get(id=user_id)
    user.id = generate_user_id(role)
    user.save(update_fields=["id"])


@shared_task
def create_user_profile(user_id):
    try:
        user = User.objects.get(id=user_id)
        if user.role == User.Roles.ADMIN:
            AdminProfile.objects.create(user=user, permissions="Full access")
        elif user.role == User.Roles.ORGANIZER:
            OrganizerProfile.objects.create(user=user, organization_name="Unknown Organization")
        elif user.role == User.Roles.ATTENDEE:
            AttendeeProfile.objects.create(user=user)
        elif user.role == User.Roles.GUEST:
            GuestProfile.objects.create(user=user, temp_id=f"guest_{user_id}")
    except User.DoesNotExist:
        print(f"User with id {user_id} does not exist.")