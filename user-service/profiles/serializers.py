# users/serializers.py

from rest_framework import serializers
from .models import AdminProfile, OrganizerProfile, AttendeeProfile, GuestProfile
from users.utils.choices_fields import Roles


class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = ['permissions']


class OrganizerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizerProfile
        fields = ['organization_name', 'is_verified', 'verified_documents']


class AttendeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendeeProfile
        fields = ['user', 'preferences', 'created_at', 'updated_at']


class GuestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestProfile
        fields = ['temp_id', 'is_registered']


class ProfileSerializer(serializers.Serializer):
    profile = serializers.SerializerMethodField()

    def get_profile(self, obj):
        if obj.role == Roles.ADMIN:
            return AdminProfileSerializer(obj.admin_profile).data
        elif obj.role == Roles.ORGANIZER:
            return OrganizerProfileSerializer(obj.organizer_profile).data
        elif obj.role == Roles.ATTENDEE:
            return AttendeeProfileSerializer(obj.attendee_profile).data
        elif obj.role == Roles.GUEST:
            return GuestProfileSerializer(obj.guest_profile).data
        return None
