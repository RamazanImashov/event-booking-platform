from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(models.TextChoices):
    ADMIN = 'admin', _('Administrator')
    ORGANIZER = 'organizer', _('Organizer')
    ATTENDEE = 'attendee', _('Attendee')
    GUEST = 'guest', _('Guest')