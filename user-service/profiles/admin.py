from django.contrib import admin
from .models import AdminProfile, AttendeeProfile, OrganizerProfile, GuestProfile

# Register your models here.


admin.site.register(AdminProfile)
admin.site.register(AttendeeProfile)
admin.site.register(OrganizerProfile)
admin.site.register(GuestProfile)